
import time

# --- formatUtcTimeAsIsoLocalTime -------------------------------------------------------------------------------------
def formatUtcTimeAsIsoLocalTime(t):
    localtime = time.localtime(t)
    s = time.strftime("%Y-%m-%d %H:%M:%S %Z", localtime)
    return s

