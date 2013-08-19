class baseconsole:
    def __init__(self):
        pass
        
    def bell(self):
        raise NotImplementedError

    def pos(self, x=None, y=None):
        u'''Move or query the window cursor.'''
        raise NotImplementedError

    def size(self):
        raise NotImplementedError

    def rectangle(self, rect, attr=None, fill=u' '):
        u'''Fill Rectangle.'''
        raise NotImplementedError

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
        raise NotImplementedError
    
    def getkeypress(self):
        u'''Return next key press event from the queue, ignoring others.'''
        raise NotImplementedError
        
    def write(self, text):
        raise NotImplementedError
    
    def page(self, attr=None, fill=' '):
        u'''Fill the entire screen.'''
        raise NotImplementedError

    def isatty(self):
        return True

    def flush(self):
        pass

    def clear_range(self, pos_range):
        u'''Clears range that may span to multiple lines
        pas_range is (x1,y1, x2,y2) including
        y2 >= y1
        x2 == -1 mean end of line
        '''
        w, h = self.size()
        (x1,y1, x2,y2) = pos_range
        if x2 < 0:
            x2 = w - 1
        if y2 < y1:
            return
        elif y2 == y1:
            self.rectangle((x1, y1, x2+1, y2+1))
            return
        else:
            full_rec = [0,y1, w, y2+1]
            if x1 > 0:
                self.rectangle((x1,y1, w, y1+1))
                full_rec[1] = y1+1
            if x2 < w-1:
                self.rectangle((0,y2, x2+1, y2+1))
                full_rec[3] = y2
            if full_rec[1] < full_rec[3]:
                self.rectangle(tuple(full_rec))

