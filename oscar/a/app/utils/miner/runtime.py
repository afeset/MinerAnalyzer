"""
Set of utility functions:
  floor(value, step, start=0)
  ceil(value, step, start=0)
  gmtime2a(unixtime)
  a2gmtime(s)
  dtime2a(dtime)
  a2dtime(s)
  dtimems2a(dtime):
  a2dtimems(s):
  num2h(num):
"""
import re
import operator
import time

class Matcher:
    """Wrapper over regular expression match"""
    def __init__(self, reStr):
        self.myRegexp = re.compile(reStr)
        self.myMatches = None
    def getGroupNames(self):
        return [ groupAndId[0] for groupAndId in sorted(self.myRegexp.groupindex.items(), key=operator.itemgetter(1))]
    def match(self, s):
        self.myMatches = self.myRegexp.search(s)
        return self.myMatches is not None
    def __len__(self):
        return len(self.myRegexp.groupindex)
    def __getitem__(self, key):
        return self.myMatches.group(key)

class Counter:
    """In command counter"""
    def __init__(self):
        self.val = 0
    def preIncr(self):
        self.val += 1
        return self.val
    def postIncr(self):
        res = self.val
        self.val += 1
        return res
    def preDecr(self):
        self.val -= 1
        return self.val
    def postDecr(self):
        res = self.val
        self.val -= 1
        return res
    def add(self, val):
        self.val += val
        return self.val
    def sub(self, val):
        self.val -= val
        return self.val

def floor(value, step, start=0):
    """Returns the largest number smaller or equal to <value> in the steps of <step> starting from <start>"""
    return ((value-start)/step)*step + start

def ceil(value, step, start=0):
    """Returns smallest number grater or equal to <value> in the steps of <step> starting from <start>"""
    return ((value-start+step-1)/step)*step + start

def gmtime2a(unixtime):
    """Converts unix time to GMT time in format '2011-12-11 09:00:21'"""
    tm = time.gmtime(unixtime)
    s = time.strftime("%Y-%m-%d %H:%M:%S", tm)
    return s

_TIME_REXP = re.compile(r"(\d+)-(\d+)-(\d+)( (\d+):(\d+)(:(\d+))?)?")

def a2gmtime(s):
    """Converts time string in format '2011-12-11 09:00:21' (time part is optional) to GMT epoch time"""
    matches = _TIME_REXP.match(s)
    if not matches:
        return 0
    tm_year = int(matches.group(1))
    tm_mon  = int(matches.group(2))
    tm_mday = int(matches.group(3))

    if matches.group(4):
        tm_hour = int(matches.group(5))
        tm_min  = int(matches.group(6))
        tm_sec  = 0 if not matches.group(8) else int(matches.group(8))
    else:
        tm_hour = 0
        tm_min  = 0
        tm_sec  = 0
    return int(time.mktime( (tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, 0, 0, 0) )) - time.timezone


def dtime2a(dtime):
    """Converts time in seconds to 'HH:MM:SS'"""
    sec = dtime % 60
    dtime /= 60
    minute = dtime % 60
    dtime /= 60
    hour = dtime
    return "%d:%02d:%02d" % (hour, minute, sec)

def a2dtime(s):
    """Converts 'HH:MM:SS' to seconds"""
    tokens = s.split(':')
    l = len(tokens)
    if l==0:
        return 0
    elif l==1:
        return int(tokens[0])
    elif l==2:
        return int(tokens[0])*60 + int(tokens[1])
    else:
        return int(tokens[0])*3600 + int(tokens[1])*60 + int(tokens[2])

def dtimems2a(dtime):
    """Converts time in milli-seconds to 'HH:MM:SS.mmm'"""
    msec = dtime % 1000
    dtime /= 1000
    sec = dtime % 60
    dtime /= 60
    minute = dtime % 60
    dtime /= 60
    hour = dtime
    if hour > 0:
        return "%d:%02d:%02d.%03d" % (hour, minute, sec, msec)
    elif minute>0:
        return "%d:%02d.%03d" % (minute, sec, msec)
    else:
        return "%d.%03d" % (sec, msec)


def a2dtimems(s):
    """Converts 'HH:MM:SS.mmm' to milli-seconds"""
    tokens = s.split('.')
    if len(tokens) == 0:
        return 0
    elif len(tokens) == 1:
        return int(tokens[0])
    else:
        s = tokens[0]
        msec = int(tokens[1])

    tokens = s.split(':')

    l = len(tokens)
    if l==0:
        return 0
    elif l==1:
        sec = int(tokens[0])
    elif l==2:
        sec = int(tokens[0])*60 + int(tokens[1])
    else:
        sec = int(tokens[0])*3600 + int(tokens[1])*60 + int(tokens[2])

    return sec*1000 + msec

def num2h(num):
    """Number to human readable string conversion"""
    if num > 1e12:
        s = "%.2fT" % (num/1e12)
    elif num > 1e9:
        s = "%.2fG" % (num/1e9)
    elif num > 1e6:
        s = "%.2fM" % (num/1e6)
    elif num > 1e3:
        s = "%.2fK" % (num/1e3)
    elif num > 1:
        s = "%s" % num
    elif num > 1e9:
        s = "%.2fm" % (num/1e-3)
    else:
        s = "%.2fu" % (num/1e-6)
    return s
