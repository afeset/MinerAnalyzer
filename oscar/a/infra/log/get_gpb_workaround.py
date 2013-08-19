#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

from include.a.infra.log.bits.body_fragment_pb2 import MsgBodyFragmentGpbDecodedBacktrace
from include.a.infra.log.bits.body_fragment_pb2 import MsgBodyFragmentGpbSimpleBuffer
from include.a.infra.log.bits.body_fragment_pb2 import MsgBodyFragmentGpbPlainTextBuffer
from include.a.infra.log.bits.body_fragment_pb2 import MsgBodyFragmentGpbJsonTextBuffer

def getMsgBodyFragmentGpbDecodedBacktrace ():
    return MsgBodyFragmentGpbDecodedBacktrace()

def getMsgBodyFragmentGpbSimpleBuffer ():
    return MsgBodyFragmentGpbSimpleBuffer()

def getMsgBodyFragmentGpbPlainTextBuffer ():
    return MsgBodyFragmentGpbPlainTextBuffer()

def getMsgBodyFragmentGpbJsonTextBuffer ():
    return MsgBodyFragmentGpbJsonTextBuffer()

from infra.log.msg_data_pb2 import MsgDataGpb
def getMsgDataGpb ():
    return MsgDataGpb()



