#!/usr/bin/env python

# Export only these functions
__all__ = ["monotonicTimeSeconds monotonicTimeNano"]

import ctypes, os

# Use CLOCK_MONOTONIC_RAW and not CLOCK_MONOTONIC, some say this would avoid clock changes due to NTP
CLOCK_MONOTONIC = 1 # see <linux/time.h>
CLOCK_MONOTONIC_RAW = 4 # see <linux/time.h>

class timespec(ctypes.Structure):
    _fields_ = [
        ('tv_sec', ctypes.c_long),
        ('tv_nsec', ctypes.c_long)
    ]

librt = ctypes.CDLL('librt.so.1', use_errno=True)
clock_gettime = librt.clock_gettime
clock_gettime.argtypes = [ctypes.c_int, ctypes.POINTER(timespec)]

def monotonicTimeNano():
    t = timespec()
    if clock_gettime(CLOCK_MONOTONIC, ctypes.pointer(t)) != 0:
        errno_ = ctypes.get_errno()
        raise OSError(errno_, os.strerror(errno_))
    return (t.tv_sec * 1000000000) + t.tv_nsec

def monotonicTimeSeconds():
    return monotonicTimeNano() / 1000000000

if __name__ == "__main__":
    print monotonicTimeNano()

