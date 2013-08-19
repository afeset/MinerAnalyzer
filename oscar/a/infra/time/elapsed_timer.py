#
# Copyright Qwilt, 2012
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: shmulika
# 


# Bypass for PyChecker
if  __package__ is None:
    G_MODULE_NAME_ELAPSED_TIMER       = "unknown"
    G_GROUP_NAME_ELAPSED_TIMER_TIMER  = "unknown"

else:
    from . import G_MODULE_NAME_ELAPSED_TIMER
    from . import G_GROUP_NAME_ELAPSED_TIMER_TIMER

import time
from a.infra.time import monotonic_clock
from a.infra.process import processFatal


class ElapsedTimerError(Exception):
    """" error base-class for this module """
    def __init__ (self, msg):
        Exception.__init__(self, msg)

class ElapsedTimerInitError(ElapsedTimerError):
    """ Raised when errors are encountered in init methods """
    def __init__ (self, msg):
        ElapsedTimerError.__init__(self, msg)

class ElapsedTimerControlError(ElapsedTimerError):
    """ Raised when errors are encountered when trying to start the timer """
    def __init__ (self, msg):
        ElapsedTimerError.__init__(self, msg)

    
            

class ElapsedTimer:
    """ Timer that can be set for a specific interval, started, and asked whether specified interval has elapsed.
    Can also be set to be repititive
    """

########################################################################################################################
# INITIALIZATION METHODS
########################################################################################################################


    def __init__ (self, logger):
        self._log = logger.createLogger(G_MODULE_NAME_ELAPSED_TIMER, G_GROUP_NAME_ELAPSED_TIMER_TIMER)

        self._intervalNanos = None
        self._allignNanos = None
        self._isRecurrent = False
        self._isDriftless = False
        
        self._isStarted = False                

        self._effectiveStartTime = None
        self._targetTime = None
        self._highestCheckedThreshold = 0.0

        self._clock = MonotonicClock() # the default clock used by the timer


    def initInterval (self, nanos):
        """ initializes interval length in nanoseconds.
        Arguments:
            nanos - length of interval (convertable to long)
        Returns: None
        Raises: ElapsedTimerInitError, when argument is not valid
        """
        if self._isStarted:
            self._log("init-interval-failed").error("cannot init interval once start() was called")
            raise ElapsedTimerInitError("Cannot init interval once start() was called")

        try:
            self._intervalNanos = self._convertToPositiveLong(nanos)
            self._log("init-interval").debug1("init interval to: %s", self._intervalNanos)
        except ElapsedTimerInitError as err:
            self._log("init-interval-failed").exception("given argument %s is not a valid interval", nanos)
            raise err


    def initAllignment (self, nanos):
        """ initializes the allignment of the starting point of the timer.

        For example if allignment is init to 100 nanos;
        And the clock was started at 4332872 nanos,
        then the timer will allign as if start time was 4332900 (which divides by 100 nanos)

        Arguments:
            nanos - the divider by which the timer is to allign (convertable to long)
            None - if not to allign at all
        Returns: None
        Raises: ElapsedTimerInitError, when argument is not valid
        """
        if self._isStarted:
            self._log("init-allignment-failed").error("cannot init allignment once start() was called")
            raise ElapsedTimerInitError("Cannot init alligment once start() was called")

        try:
            self._allignNanos = self._convertToPositiveLong(nanos)
            self._log("init-allignment").debug1("init allignment to: %s", self._allignNanos)
        except ElapsedTimerInitError as err:
            self._log("init-allignment-failed").exception("given argument %s is not a valid allignment", nanos)
            raise err
        


    def _initClock (self, clock):
        """ initialized the clock used by the timer to get current time in nanos
        Arguments:
            clock - implementation of the ClockInterface
        Returns: None
        Raises: ElapsedTimerInitError, when argument is not valid
        """
        if self._isStarted:
            self._log("init-clock-failed").error("cannot init clock once start() was called")
            raise ElapsedTimerInitError("Cannot init clock once start() was called")

        try:
            self._convertToNonNegativeLong(clock.getNowInNanos())
            self._clock = clock
            self._log("init-clock").debug1("clock was inited")
        except:
            self._log("init-clock-failed").exception("given argument does not implement ClockInterface")
            raise ElapsedTimerInitError("clock must implement ClockInterface")
        

    def initRecurrence (self, isDriftless):
        """ initializes whether this timer should be recurrent or one-shot.

        If one-shot (this method not called), then once elapsed time is passed, hasElapsed will always return True
        If recurrent (this method called), then hitting the elapsed time (by hasElapsed) will reset the timer for the next interval.

        A non-driftless recurrent timer calculates a new elapse time according to the current time.
        A driftless recurrent timer makes sure that a new elapse time is no a fixed grid of constant intervals from the
        original start time.          

        Non-driftless: |----+----|--+----|+----|---+----|   (where | is elapse time, and + is check points, elapse time determined by check point)

        Drifltess:     |---+|-+--|+---|--+-|-+--|+---|--+-| (elapse time not determined by check point)


        Arguements:
            isDriftless - boolean, if True - the timer will be driftless

        Returns: None
        Raises: ElapsedTimerInitError, when argument is not valid
        """
        if self._isStarted:
            self._log("init-recurrence-failed").error("cannot init recurrence once start() was called")
            raise ElapsedTimerInitError("Cannot init recurrence once start() was called")

        try:
            self._isRecurrent = True

            if isDriftless:
                self._isDriftless = True
            else:
                self._isDriftless = False
            
            self._log("init-recurrence").debug1("init recurrent with driftless: %s", self._isDriftless)

        except:
            self._log("init-recurrence-failed").error("isDriftless should be a boolean")
            raise ElapsedTimerInitError("shouldRecur should be a boolean (or behave like one)")


########################################################################################################################
# CONTROL METHODS
########################################################################################################################  

    def start (self):
        """ Starts the timer now
        Returns: None
        Raises: ElapsedTimerControlError, if called when not initialized properly
        """
        if self.wasStarted():
            self._log("start-failed").error("cannot start again once start() was called")
            raise ElapsedTimerControlError("Timer was already started")

        if self._intervalNanos is None:
            self._log("start-failed").error("initInterval must be called before start")
            raise ElapsedTimerControlError("Must call initInterval before start")

        self._resetTimer()

        self._isStarted = True
        self._log("start").debug1("timer was started")


    def restart (self):
        """ Restarts the timer now
        Returns: None
        Raises: ElapsedTimerControlError, if called when not started yet
        """
        if not self.wasStarted():
            self._log("restart-failed").error("Timer wasn't started yet, cannot restart")
            raise ElapsedTimerControlError("Timer wasn't started yet, cannot restart")

        self._resetTimer()
        self._log("restart").debug1("timer was restarted")
        

    def wasStarted (self):
        """ Returns: True if timer was started succesfully """
        self._log("was-started").debug4("getting was-started: %s", self._isStarted)
        return self._isStarted


    

    def hasCrossedThresholdForFirstTime (self, threshold):        
        """ Checks whether a specific fraction of the interval (threshold) was crossed,
        The method checks if that threshold was crossed, and returns True only for the first time it was crossed.

        For example:
            hasCrossedThresholdForFirstTime(0.33) will return True if third of the interval was crossed,
            but another call to hasCrossedThresholdForFirstTime(0.33) or lower value (like 0.2) will return False.

        The "threshold memory" is reset, when restarting the timer, or after hasElapsed / countElapsed returned True / >0.

        Notice that this method will never reset the timer!!!!

        Example usage:

            if timer.hasElapsed():
                log("elapsed-timeout").error("timeout elapsed, the machine is broken!!!")
            
            if timer.hasCrossedThresholdForFirstTime(0.5):
                log("half-timeout").warning("half of the timeout has passed!!")

            if timer.hasCrossedThresholdForFirstTime(0.33):
                log("third-timeout").notice("third of the timeout has passed")

            if timer.hasCrossedThresholdForFirstTime(0.25):
                log("quarter-timeout").debug1("quarter of the timeout has passed")            


        Argurments:
            threshold - float, fraction; 0 < threshold < 1

        Returns: True if threshold was crossed for the first time
        Raises: ElapsedTimerControlError, if called when not started yet, or if argument value is invalid
        """        

        try:
            threshold = float(threshold)
        except:
            self._log("has-elapsed-threshold-failed").error("expecting float as threshold, but %s was given", threshold)
            raise ElapsedTimerControlError("threshold must be a float")

        if threshold <= 0 or threshold >= 1:
            self._log("has-elapsed-threshold-failed").error("threshold must be 0 < .. < 1, but %s was given", threshold)
            raise ElapsedTimerControlError("threshold must be 0 < .. < 1")


        if threshold <= self._highestCheckedThreshold:
            self._log("has-elapsed-threshold-already").debug3("threshold %s has already been checked by threshold %s", threshold, self._highestCheckedThreshold)
            return False

        countIntervals, deltaNextElapse, nowNanos = self._countElapsedNoReset()

        if deltaNextElapse >= self._intervalNanos:
            percentageCompletion = 0.0
        else:
            percentageCompletion = (float(self._intervalNanos) - float(deltaNextElapse)) / float(self._intervalNanos)

        if percentageCompletion >= threshold:
            self._highestCheckedThreshold = threshold
            self._log("has-elapsed-threshold-elapsed").debug3("threshold %s elapsed at time %s, with %s completion", threshold, nowNanos, percentageCompletion)
            return True           

        self._log("has-elapsed-threshold-not").debug3("threshold %s not elapsed at time %s, with %s completion", threshold, nowNanos, percentageCompletion)
        return False



    def hasElapsed (self):
        """ Returns: True if timer has elapsed

        For no-repetitive timers, hasElapsed will continue to return True after elapse time has passed
        For repetitive timers, hasElapsed will return True, then recalculate next elapse time, till which will be False.

        If timer not started yet, returns False.
        Raises: ElapsedTimerControlError, if called when not started yet
        """
        countIntervals = self.countElapsed()

        return countIntervals > 0

        
    def countElapsed (self):
        """ returns the number of intervals fully elapsed since effective start time
        In case of non-recurrent timers, this can be only 0 or 1
        In case of reccurent timers, can be any integer

        Returns: intervals
        Raises: ElapsedTimerControlError, if called when not started yet
        """
        countIntervals, deltaNanos, nowNanos = self._countElapsedNoReset()

        self._log("count-elapsed").debug2("intervals elapsed: %s", countIntervals)

        if countIntervals > 0 and self._isRecurrent:
            self._log("count-elapsed-reset-timer").debug2("recurrent: resetting the timer at %s", nowNanos)
            self._retargetTimerNow(nowNanos, countIntervals)
        
        return countIntervals



    def sleepTillElapsedCount (self):
        """ Sleeps until the timeout has elasped, and returns the number of intervals fully elapsed (like countElapsed method)

        Returns: intervals
        Raises: ElapsedTimerControlError, if called when not started yet
        """
        countIntervals, passedSeconds = self.sleepTillElapsedCountAndSeconds()
        return countIntervals


    def sleepTillElapsedPassedSeconds (self):
        """ Sleeps until the timeout has elasped, and returns the number of seconds passed since the actual target time till awakening from the sleep.

        Returns: seconds (float)
        Raises: ElapsedTimerControlError, if called when not started yet
        """
        countIntervals, passedSeconds = self.sleepTillElapsedCountAndSeconds()
        return passedSeconds


    def sleepTillElapsedCountAndSeconds (self):
        """ Sleeps until the timeout has elasped, and returns the number of intervals fully elapsed (like countElapsed method), and the number of seconds passed since the target time

        Returns: intervals, seconds since target time
        Raises: ElapsedTimerControlError, if called when not started yet
        """
        intervals, delta, nowNanos = self._countElapsedNoReset()
        deltaSeconds = self.nanosToSeconds(delta)
        while deltaSeconds > 0:                    
            self._log("sleep-till-elapsed-count-and-seconds-not-elapsed-yet").debug2("sleeping %s seconds until target-time", deltaSeconds)
            time.sleep(deltaSeconds)
            intervals, delta, nowNanos = self._countElapsedNoReset()
            deltaSeconds = self.nanosToSeconds(delta)
            

        passedSeconds = self.nanosToSeconds(nowNanos - self._targetTime)        
        countIntervals = self.countElapsed()
        self._log("sleep-till-elapsed-count-and-seconds-elapsed").debug2("target-time was %s seconds ago", passedSeconds)

        return countIntervals, passedSeconds





    def _countElapsedNoReset (self):
        """ counts how many intervals have passed since last reset, and how many nanos are until next elapse time (delta).
        does not cause a timer reset when elapse time has passed (even if recurrent).

        If elapse time has passed, then delta will be zero.

        Returns: (intervals, delta, nowNanos)
        Raises: ElapsedTimerControlError, if called when not started yet
        """
        if not self.wasStarted():
            self._log("count-elapsed-no-reset-failed").error("was not started yet")
            raise ElapsedTimerControlError("Timer wasn't started yet")

        nowNanos = self._clock.getNowInNanos()

        if nowNanos >= self._targetTime:            
            deltaNanos = 0

            if self._isRecurrent:
                countIntervals = 1 + (nowNanos - self._targetTime) / self._intervalNanos # this is the full number of intervals elapsed
            else:
                countIntervals = 1
         
        else:
            countIntervals = 0
            deltaNanos = self._targetTime - nowNanos

        self._log("count-elapsed-no-reset").debug3("elapsed intervals: %s, delta to next: %s", countIntervals, deltaNanos)
        return (countIntervals, deltaNanos, nowNanos)


    def _resetTimer (self):
        """ called when the timer is started or restarted """

        self._actualStartTime = self._clock.getNowInNanos()

        # if this is the first time and allignment is set - allign the effective start time
        if self._allignNanos is not None:
            self._effectiveStartTime = self._allignUpTo(self._actualStartTime, self._allignNanos)
        else:
            self._effectiveStartTime = self._actualStartTime

        self._targetTime = self._effectiveStartTime + self._intervalNanos                

        self._highestCheckedThreshold = 0.0

        self._log("reset-timer-now").debug2("actual start time: %s; effective start time: %s; elapse time: %s", self._actualStartTime, self._effectiveStartTime, self._targetTime)


    def _retargetTimerNow (self, nowNanos, intervalsElapsed):
        """ sets the target time of the timer, according to the current time in nanos, and how many intervals have lapsed since last target time
        """
        self._actualStartTime = nowNanos
        self._effectiveStartTime = self._actualStartTime

        if self._isDriftless:
            self._targetTime = self._targetTime + intervalsElapsed * self._intervalNanos
        else:
            self._targetTime = self._effectiveStartTime + self._intervalNanos

        self._highestCheckedThreshold = 0.0

        self._log("retarget-timer-now").debug2("actual start time: %s; effective start time: %s; elapse time: %s", self._actualStartTime, self._effectiveStartTime, self._targetTime)





########################################################################################################################
# NON-MUTABLE GETTERS
########################################################################################################################  


    def getInterval (self):
        """ Returns: the interval that was set for the timer in nanos, as integer """
        self._log("get-interval").debug2("getting interval %s", self._intervalNanos)
        return self._intervalNanos


    def getEffectiveStartTime (self):
        """ Gets the effective start time in nanos, which is the time in which the timer is considered started after
        taking allignment into consideration
        Returns: time in nano
        Raises: ElapsedTimerControlError, if called when not started yet
        """
        if not self.wasStarted():
            self._log("get-effective-start-time-none").error("timer not started yet")
            raise ElapsedTimerControlError("Timer wasn't started yet")
        
        self._log("get-effective-start-time").debug2("getting effective-start-time %s", self._effectiveStartTime)
        return self._effectiveStartTime


    def getTargetTime (self):
        """Returns: target time in nano, time after which timer is considered elapsed
        Raises: ElapsedTimerControlError, if called when not started yet
        """

        if not self.wasStarted():
            self._log("get-target-time-none").error("timer not started yet")
            raise ElapsedTimerControlError("Timer wasn't started yet")
        
        self._log("get-target-time").debug2("getting target-time %s", self._targetTime)
        return self._targetTime
    

########################################################################################################################
# UTILITY METHODS
########################################################################################################################

    _NANOS_IN_ONE_SECOND = 1000000000

    def secondsToNanos (self, seconds):
        """ Converts seconds into nanoseconds """
        return long(seconds * self._NANOS_IN_ONE_SECOND)


    def nanosToSeconds (self, nanos):
        """ Converts nanos to seconds """
        return float(nanos) / self._NANOS_IN_ONE_SECOND



    def _convertToPositiveLong (self, nanos):
        nanos = self._convertToNonNegativeLong(nanos)

        if nanos == 0:
            raise ElapsedTimerInitError("nanos must be greater than zero, but %s was given"%nanos)

        return nanos


    def _convertToNonNegativeLong (self, nanos):
        try:
            nanos = long(nanos)

        except:
            raise ElapsedTimerInitError("nanos must be convertable to long, but %s was given"%nanos)

        if nanos < 0:
            raise ElapsedTimerInitError("nanos must not be negative, but %s was given"%nanos)

        return nanos


    def _allignUpTo (self, value, allignment):
        """ Rounds a given value up, so it alligns with a given allignment divider.

        For example:
            If value is 145 and allignemnt is 100, returns 200
            If value is 145 and allignemnt is 50, returns 150

        Arguments:
            value - integer,
            allignment - integer
        Returns:
            alligned value - integer
        """
        remainder = value % allignment
        if remainder == 0: # alligned
            return value
        else:
            return value + allignment - remainder
        



########################################################################################################################
# CLOCK INTERFACE
########################################################################################################################

class ClockException:
    """ Exception base raised by clock implementations """
    def __init__ (self, msg):
        self.msg = msg
            

class ClockInterface:
    def __init__ (self):
        pass

    def getNowInNanos (self):
        """ Returns: current time in nanoseconds (integer)"""
        __pychecker__ = 'unusednames=self'
        processFatal("method not implemented")


class MonotonicClock(ClockInterface):
    def __init__ (self):
        ClockInterface.__init__(self)        
    
    def getNowInNanos (self):
        """ Returns: current time in nanoseconds (integer)"""        
        return monotonic_clock.monotonicTimeNano()


