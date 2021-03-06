import sys
import atexit
import os
import re

from pyreadline.logger import log
from consolebase import *
from pyreadline.keysyms.ansi_keysyms import KeyPressReader, sequence2KeyPress
from event import Event

_terminalWasInitialized = False

_oldTerminalAttributes = None

_stdinFd = sys.stdin.fileno()

def setupTerminal():
    import termios, tty
    global _terminalWasInitialized
    global _oldTerminalAttributes
    global _stdinFd
    if _terminalWasInitialized:
        return
    _oldTerminalAttributes = termios.tcgetattr(_stdinFd)
    try:
        #tty.setraw(fd)
        new = termios.tcgetattr(_stdinFd)
        new[0] = new[0] & ~(termios.INLCR | termios.IGNCR | termios.ICRNL)
        new[3] = new[3] & ~(termios.ECHO | termios.ICANON)    # lflags
        new[6][termios.VTIME] = 0
        new[6][termios.VMIN] = 0
        new[6][termios.VSUSP] = 0
        termios.tcsetattr(_stdinFd, termios.TCSADRAIN, new)
        _terminalWasInitialized = True
        atexit.register(restoreTerminal, _oldTerminalAttributes)
    except Exception as e:
        print "Failed to setup terminal:", e
        termios.tcsetattr(_stdinFd, termios.TCSADRAIN, _oldTerminalAttributes)
        raise

def restoreTerminal(oldAttrs):
    import termios
    termios.tcsetattr(_stdinFd, termios.TCSADRAIN, oldAttrs)

class event(Event):
    def __init__(self, keyPress):
        self.type = u"KeyPress"
        self.char = keyPress.char
        if len(self.char) == 0:
            self.char = '\000'
        self.keycode = 0
        self.state = 0
        self.keyinfo = keyPress
        self.keysym = u'??'

class Console(baseconsole):
    def __init__(self):
        baseconsole.__init__(self)
        setupTerminal()
        self.fd = sys.stdin.fileno()
        self.keyReader = KeyPressReader()
        self.saveattr = 0 # required by Readline
        self.position = None
        self.windowSize = None

    #def __del__(self):
    #    restoreTerminal()
        
    def bell(self):
        self.write("\a")
    
    def pos(self, x=None, y=None):
        log(u"ansi_console.pos(%s, %s)" % (x, y))
        if x is not None and y is not None:
            self._setPos(x, y)
            return (x, y)
        else:
            (oldX, oldY) = self._queryPos()
            if x is not None or y is not None:
                needToUpdate = True
            else:
                needToUpdate = False
            if x is None:
                x = oldX
            if y is None:
                y = oldY
            if needToUpdate:
                self._setPos(x, y)
            return (x, y)

    def _write(self, s):
        return os.write(self.fd, s)

    def write(self, s):
        if s == "\r\n":
            log("write('\\r\\n')")
            # reset window size each time we enter new line
            self.windowSize = None
        else:
            log("write('%s')" % s)
        
        self.position = None
        return self._write(s)

    terminal_escape = re.compile(u'(\001?\033\\[[0-9;]*m\002?)')
    escape_parts = re.compile(u'\001?\033\\[([0-9;]*)m\002?')

    # This pattern should match all characters that change the cursor position differently
    # than a normal character.
    motion_char_re = re.compile(u'([\n\r\t\010\007])')

    def write_scrolling(self, text, attr=None):
        u'''write text at current cursor position while watching for scrolling.

        If the window scrolls because you are at the bottom of the screen
        buffer, all positions that you are storing will be shifted by the
        scroll amount. For example, I remember the cursor position of the
        prompt so that I can redraw the line but if the window scrolls,
        the remembered position is off.

        This variant of write tries to keep track of the cursor position
        so that it will know when the screen buffer is scrolled. It
        returns the number of lines that the buffer scrolled.

        '''
        log(u"write_scrolling('%s') # len=%d" % (text, len(text)))
        x, y = self.pos()
        self.position = None
        w, h = self.size()
        scroll = 0 # the result

        # split the string into ordinary characters and funny characters
        chunks = self.motion_char_re.split(text)
        for chunk in chunks:
            n = self._write(chunk)
            log(u"# self._write(chunk) = %d" % n)
            if len(chunk) == 1: # the funny characters will be alone
                if chunk[0] == u'\n': # newline
                    x = 0
                    y += 1
                elif chunk[0] == u'\r': # carriage return
                    x = 0
                elif chunk[0] == u'\t': # tab
                    x = 8 * (int(x / 8) + 1)
                    if x > w: # newline
                        x -= w
                        y += 1
                elif chunk[0] == u'\007': # bell
                    pass
                elif chunk[0] == u'\010':
                    x -= 1
                    if x < 0:
                        y -= 1 # backed up 1 line
                else: # ordinary character
                    x += 1
                if x == w: # wrap
                    x = 0
                    y += 1
                if y == h: # scroll
                    scroll += 1
                    y = h - 1
            else: # chunk of ordinary characters
                x += n
                l = int(x / w) # lines we advanced
                x = x % w # new x value
                y += l
                if y >= h: # scroll
                    scroll += y - h + 1
                    y = h - 1
        log(u"# return write_scrolling('%s') = %d" % (text, scroll))
        # no scrolling occured so we can safely (until size is changed during line exiting)
        if x == 0 and scroll==0:
            self.position = None
        else:
            self.position = (x, y)
        log("# position updated to %s" % str(self.position))
        return scroll

    def _setPos(self, x, y):
        if self.position == (x, y):
            return
        self._write("\033[%d;%dH"%(y+1,x+1))
        self.position = (x,y)
        log("_setPos%s" % str(self.position))

    def _queryPos(self):
        if self.position:
            log("_queryPos() # cached value = " + str(self.position))
            return self.position
        self._write("\033[6n")
        for repeat in range(10):
            res = self.keyReader.getCursorPosition(0.1)
            if res:
                break
        if not res:
            return (0,0)
        else:
            self.position = (res[1]-1, res[0]-1)
            log("_queryPos() # = " + str(self.position))
            return self.position

    def _readIntFromCmd(self, cmd):
        pipe = os.popen(cmd, 'r')
        s = pipe.readline()
        val = int(s.strip())
        pipe.close()
        return val
        
    def size(self):
        log("size()")
        if self.windowSize:
            log("# returned cached value %s" % str(self.windowSize))
            return self.windowSize
        w = self._readIntFromCmd("tput cols")
        h = self._readIntFromCmd("tput lines")
        self.windowSize = (w,h)
        log("size() # = " + str(self.windowSize))
        return (w, h)

    def getkeypress(self):
        return event(self.keyReader.getKey())

    def clear_state(self):
        """clean internal states"""
        self.position = None
        self.windowSize = None
    
    def page(self, attr=None, fill=u' '):
        u'''Fill the entire screen.'''
        self._write("\033[2J\033[H")
        self.position = (0,0)

    def rectangle(self, rect, attr=None, fill=u' '):
        u'''Fill Rectangle.'''
        log("rectangle(%s, fill='%s')" % (rect, fill))
        oldpos = self.pos()
        #raise NotImplementedError
        x0, y0, x1, y1 = rect
        if fill:
            rowfill = fill[:1] * abs(x1 - x0)
        else:
            rowfill = u' ' * abs(x1 - x0)
        for y in range(y0, y1):
                self.pos(x0, y)
                self._write(rowfill)
        self.position = None
        self.pos(*oldpos)

    def clear_range(self, pos_range):
        u'''Clears range that may span to multiple lines
        pos_range is (x1,y1, x2,y2) including
        y2 >= y1
        x2 == -1 means end of line
        '''
        log("clearRange(%s)" % str(pos_range))
        (x1,y1, x2,y2) = pos_range
        if y2 < y1:
            return
        elif y2 == y1 and x2>=0:
            self.pos(x1,y1)
            self._write(' '*(x2-x1+1))
        else:
            start = y1
            end = y2+1
            if x1 > 0:
                self.pos(x1,y1)
                self._write("\033[0K")
                start = y1+1
            if 0 <= x2 < w-1:
                self.pos(x2,y2)
                self._write("\033[1K")
                end = y2
            for line in range(start, end):
                self.pos(0,line)
                self._write("\033[2K")
        self.position = None
        self.pos(x1,y1)
    
    def cursor(self, visible=None, size=None):
        log("cursor(visible='%s')" % visible)
        if visible is not None:
            if visible:
                self._write("\033[?25h")
            else:
                self._write("\033[?25l")

    def scroll(self, rect, dx, dy, attr=None, fill=' '):
        u'''Scroll a rectangle.'''
        raise NotImplementedError

    def scroll_window(self, lines):
        log("scroll_window(%d)" % lines)
        if lines<0:
            self._write("\033[%dS" % -lines)
        elif lines>0:
            self._write("\033[%dT" % lines)
            

def install_readline(hook):
    log("Installing ansi_console")
    global _old_raw_input
    if _old_raw_input is not None:
        return # don't run _setup twice

    try:
        f_in = sys.stdin.fileno()
        f_out = sys.stdout.fileno()
    except (AttributeError, ValueError):
        return
    if not os.isatty(f_in) or not os.isatty(f_out):
        return

    if '__pypy__' in sys.builtin_module_names:    # PyPy

        def _old_raw_input(prompt=''):
            # sys.__raw_input__() is only called when stdin and stdout are
            # as expected and are ttys.  If it is the case, then get_reader()
            # should not really fail in _wrapper.raw_input().  If it still
            # does, then we will just cancel the redirection and call again
            # the built-in raw_input().
            try:
                del sys.__raw_input__
            except AttributeError:
                pass
            return raw_input(prompt)
        sys.__raw_input__ = hook

    else:
        # this is not really what readline.c does.  Better than nothing I guess
        import __builtin__
        _old_raw_input = __builtin__.raw_input
        __builtin__.raw_input = hook

_old_raw_input = None

if __name__ == '__main__':
    import time, sys

    c = Console()
    sys.stdout = c
    sys.stderr = c
    windowSize = c.size()
    iniPos = c.pos()
    c.page()
    c.write("window size      - "+ str(windowSize))
    c.write("\r\n")
    print "initial position -", iniPos
    c.pos(5, 10)
    c.write('hi there')
    pos = c.pos()
    print 'some printed output'
    print 'Position after "hi there" is: ', pos
    for y in range(20):
        c.pos(0, y)
        c.write("%2d "% y)
    
    c.pos(4, 14)
    c.write("Clear lines 15, 16")
    c.clear_range((0,15,-1,16))
        
    c.pos(0, windowSize[1]-1)
    c.cursor(visible=0)
    c.write_scrolling("  this is last line")
    c.pos(None, None)
    c.write_scrolling('>>> ') # len=4
    c.pos(None, None)
    # return write_scrolling('>>> ') = 0
    c.pos(None, None)
    c.cursor(visible='0')
    c.pos(0, 29)
    c.pos(None, None)
    c.write_scrolling('>>> ') # len=4
    c.pos(None, None)
    # return write_scrolling('>>> ') = 0
    c.pos(None, None)
    c.write_scrolling('') # len=0
    c.pos(None, None)
    # return write_scrolling('') = 0
    c.pos(None, None)
    c.pos(None, None)
    c.pos(None, None)
    c.pos(4, 29)
    c.pos(4, 29)
    c.pos(None, None)
    c.pos(4, 29)
    c.cursor(visible='1')
    c.pos(4, 29)

    iniPos = c.pos()
    c.pos(iniPos[0], iniPos[1])
    c.cursor(visible=1)
    c.pos(iniPos[0], iniPos[1])
    c.pos(0, 12)
    for i in range(10):
        q = c.getkeypress()
        print q
    c.rectangle((pos[0], pos[1]+1, pos[0]+10, pos[1]+10))
    del c

