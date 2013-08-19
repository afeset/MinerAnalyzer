#Shamelessly based on code from http://code.activestate.com/recipes/278731-creating-a-daemon-the-python-way/


# Standard Python modules.
import os               # Miscellaneous OS interfaces.
import signal

pidFileName=None

#import sys              # System-specific parameters and functions.
#def removePidFileAndExit():
#    #this function is based on the global pidFileName created on the daemonize function
#    #please use with care
#    print "DaemonUtils::removePidFileAndExit() called."
#    if pidFileName != None:
#        try:
#            print "Removing pid file '"+pidFileName+"'...."
#            if os.path.exists(pidFileName):
#                os.remove(pidFileName)
#        except:
#            pass
#    print "Calling sys.exit(0). Bye !"
#    sys.exit(0)

def setProcessName(newname):   
    from ctypes import cdll, byref, create_string_buffer 
    libc = cdll.LoadLibrary('libc.so.6')    
    buff = create_string_buffer(len(newname)+1)
    buff.value = newname                 
    libc.prctl(15, byref(buff), 0, 0, 0)

    
# Default daemon parameters.
# File mode creation mask of the daemon.
UMASK = 0

# Default working directory for the daemon.
# Since the current working directory may be a mounted filesystem, we
# avoid the issue of not being able to unmount the filesystem at
# shutdown time by changing it to the root directory. (unless a path was specified by the user)
WORKDIR = "/"

# Default maximum for the number of available file descriptors.
MAXFD = 1024

def daemonizeMe(stdoutFile="/dev/null", pidFile=None, workDir=WORKDIR, processName = None, doOnExit = None, waitPid = False):
   """Detach a process from the controlling terminal and run it in the
   background as a daemon.
   """

   global pidFileName
   pidFileName=pidFile

   try:
      # Fork a child process so the parent can exit.  This returns control to
      # the command-line or shell.  It also guarantees that the child will not
      # be a process group leader, since the child receives a new process ID
      # and inherits the parent's process group ID.  This step is required
      # to insure that the next call to os.setsid is successful.
      pid = os.fork()
   except OSError, e:
      raise Exception, "%s [%d]" % (e.strerror, e.errno)

   if (pid == 0): # The first child.
      # To become the session leader of this new session and the process group
      # leader of the new process group, we call os.setsid().  The process is
      # also guaranteed not to have a controlling terminal.
      os.setsid()

      # Is ignoring SIGHUP necessary?
      #
      # It's often suggested that the SIGHUP signal should be ignored before
      # the second fork to avoid premature termination of the process.  The
      # reason is that when the first child terminates, all processes, e.g.
      # the second child, in the orphaned group will be sent a SIGHUP.
      #
      # "However, as part of the session management system, there are exactly
      # two cases where SIGHUP is sent on the death of a process:
      #
      #   1) When the process that dies is the session leader of a session that
      #      is attached to a terminal device, SIGHUP is sent to all processes
      #      in the foreground process group of that terminal device.
      #   2) When the death of a process causes a process group to become
      #      orphaned, and one or more processes in the orphaned group are
      #      stopped, then SIGHUP and SIGCONT are sent to all members of the
      #      orphaned group." [2]
      #
      # The first case can be ignored since the child is guaranteed not to have
      # a controlling terminal.  The second case isn't so easy to dismiss.
      # The process group is orphaned when the first child terminates and
      # POSIX.1 requires that every STOPPED process in an orphaned process
      # group be sent a SIGHUP signal followed by a SIGCONT signal.  Since the
      # second child is not STOPPED though, we can safely forego ignoring the
      # SIGHUP signal.  In any case, there are no ill-effects if it is ignored.
      #
      # import signal           # Set handlers for asynchronous events.
      # signal.signal(signal.SIGHUP, signal.SIG_IGN)

      try:
         # Fork a second child and exit immediately to prevent zombies.  This
         # causes the second child process to be orphaned, making the init
         # process responsible for its cleanup.  And, since the first child is
         # a session leader without a controlling terminal, it's possible for
         # it to acquire one by opening a terminal in the future (System V-
         # based systems).  This second fork guarantees that the child is no
         # longer a session leader, preventing the daemon from ever acquiring
         # a controlling terminal.
         pid = os.fork() # Fork a second child.
      except OSError, e:
         raise Exception, "%s [%d]" % (e.strerror, e.errno)

      if (pid == 0): # The second child.
         os.chdir(workDir)
         # We probably don't want the file mode creation mask inherited from
         # the parent, so we give the child complete control over permissions.
         os.umask(UMASK)
      else:
         # exit() or _exit()?  See below.
         os._exit(0) # Exit parent (the first child) of the second child.
   else:
      if waitPid:
          #waiting for the new process to be created. As it shall finish rather quickly, we wait for it to exit
          #This wait can be combined with a "waitpid" on the using module in order to solve issues in which the parent 
          #returns to quickly, before the forked childs are demonized, and the to-be daemons therefore die
          os.waitpid(pid, 0)
      # exit() or _exit()?
      # _exit is like exit(), but it doesn't call any functions registered
      # with atexit (and on_exit) or any registered signal handlers.  It also
      # closes any open file descriptors.  Using exit() may cause all stdio
      # streams to be flushed twice and any temporary files may be unexpectedly
      # removed.  It's therefore recommended that child branches of a fork()
      # and the parent branch(es) of a daemon use _exit().
      os._exit(0) # Exit parent of the first child.

   deattachAllFds(stdoutFile)

   try:
     # Fork so we also have a process that monitors the actual worker processes
     # and print the exit code to stdout
     pid = os.fork() # Fork a second child.
   except OSError, e:
      raise Exception, "%s [%d]" % (e.strerror, e.errno)

   if (pid == 0): # The hard working child.
      if processName:
          setProcessName(processName)
   else:
      if processName:
          setProcessName("p_"+processName)
      (pid, rc) = os.waitpid(pid, 0)
      if not doOnExit is None:
          #The parent - monitoring the child and wait for a return code          
          doOnExit(pid = pid, rc = rc)          
      # exit() or _exit()?  See below.
      os._exit(0) # Exit parent (third child)

   # Create pid file
   if pidFileName:
       pidFile=open(pidFileName, "w")
       pidFile.write("%s\n" % os.getpid())
       pidFile.close()

   return(0)



#deattach all opened file descriptors, and specifically redirecting stdout and stderr into a file
def deattachAllFds(stdoutFile="/dev/null"):
   # Close all open file descriptors.  This prevents the child from keeping
   # open any file descriptors inherited from the parent.  There is a variety
   # of methods to accomplish this task.  Three are listed below.
   #
   # Try the system configuration variable, SC_OPEN_MAX, to obtain the maximum
   # number of open file descriptors to close.  If it doesn't exists, use
   # the default value (configurable).
   #
   # try:
   #    maxfd = os.sysconf("SC_OPEN_MAX")
   # except (AttributeError, ValueError):
   #    maxfd = MAXFD
   #
   # OR
   #
   # if (os.sysconf_names.has_key("SC_OPEN_MAX")):
   #    maxfd = os.sysconf("SC_OPEN_MAX")
   # else:
   #    maxfd = MAXFD
   #
   # OR
   #
   # Use the getrlimit method to retrieve the maximum file descriptor number
   # that can be opened by this process.  If there is not limit on the
   # resource, use the default value.
   #
   import resource # Resource usage information.
   maxfd = resource.getrlimit(resource.RLIMIT_NOFILE)[1]
   if (maxfd == resource.RLIM_INFINITY):
      maxfd = MAXFD

   # Iterate through and close all file descriptors.
   for fd in range(0, maxfd):
      try:
         os.close(fd)
      except OSError: # ERROR, fd wasn't open to begin with (ignored)
         pass

   # Redirect the standard I/O file descriptors to the specified file.  Since
   # the daemon has no controlling terminal, most daemons redirect stdin,
   # stdout, and stderr to /dev/null.  This is done to prevent side-effects
   # from reads and writes to the standard I/O file descriptors.

   # This call to open is guaranteed to return the lowest file descriptor,
   # which will be 0 (stdin), since it was closed above.
   os.open("/dev/null", os.O_RDONLY)    # standard input (0)

   # This call to open is guaranteed to return the lowest file descriptor,
   # which will be 1 (stdout), since it was closed above.
   os.open(stdoutFile, os.O_WRONLY | os.O_APPEND | os.O_CREAT) # standard output (1)

   # Duplicate standard output to standard error.
   os.dup2(1, 2) # standard error (2)


def getPid (pidFile):
    try:
        f=open(pidFile)
    except:
        # no pid file - good, return 0
        return 0
    pids=f.readline().strip()
    try:
        pid=int(pids)
    except ValueError:
        return 0
    return pid


# Returns (code, message, pid).
# code:    1 if daemon is up (Looks at pid file and process name),
#          0 if daemon is down normally (no pid file)
#          2 if daemon is crashed (pid file exists and process does not exist or does not match the supplied name)
# message: None if daemon status is normal (i.e. pid file exists and process is up and ok, or pid file does not exist)
#          Otherwise, contains a helpfull message
# pid:     when code=0, contains the pid (As an integer)
def checkStatus (pidFile, name=None):
    try:
        f=open(pidFile)
    except:
        # no pid file - good, return 0
        return (0,None,0)
    pids=f.readline().strip()
    try:
        pid=int(pids)
    except ValueError:
        return (2, "pid file '"+pidFile+"' contains non-numeric data '"+pids+"'", 0)

    f.close()
    if not os.path.exists("/proc/"+pids):
        return (2,"pid file exists, but /proc/"+pids+" does not exist",0)

    if not name is None:
        try:
            f=open("/proc/"+pids+"/cmdline")
        except:
            if not os.path.exists("/proc/"+pids):
                #process has just went down...
                return (2,"pid file exists, but /proc/"+pids+" does not exist",0)
            # no cmdline file - seems like something is fishy
            return (2,"WIERD: pid file exists, containing "+pids+", and /proc/"+pids+" exists, but /proc/"+pids+"/cmdline does not exist",0)
        try:
            cmdline=f.readline()
            f.close()
        except:
            if not os.path.exists("/proc/"+pids):
                #process has just went down...
                return (2,"pid file exists, but /proc/"+pids+" does not exist",0)
            return (2,"WIERD: failed to read or close the pid file /proc/"+pids,0)

        if cmdline.find(name)==-1:
            return (2,"pid file exists, containing "+pids+", but /proc/"+pids+"/cmdline does not contain '"+name+"'",0)

    # Passed all tests, report daemon is up
    return (1,None,pid)

# Kills a daemon given it's pid file
def killDaemon (pidFile, sigNum=signal.SIGINT):
    (up,msg,pid)=checkStatus(pidFile)
    if up:
        os.kill(pid, sigNum)


