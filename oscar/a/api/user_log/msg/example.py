#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

from message_base import declareMessage, MessageBase
                
# A message to be create by "a.api.user_log.msg.example.SimpleExample()"
# Of Severity "notification", category "CATEGORY", group "GROUP", code "CODE"
# and text: "text to be sent to the log"
SimpleExample = declareMessage(
"""
This message is created whenever ...
@version: 
@format: Text to be sent to the log
""", 
MessageBase.STATE_DECLARED,

    MessageBase.WARNING, 
    "CATEGORY", "GROUP", "CODE",
    "Text to be sent to the log")

# A message to be create by "a.api.user_log.msg.example.ParametersExample(inputString, inputNumber)"
# Of Severity "notification", category "CATEGORY", group "GROUP", code "CODE"
# and a customized text that embed a string and a number
ParametersExample = declareMessage(
"""
This message is created whenever...
@version: 
@format: A string [str] and a number [num] are sent to the log
@param str: the string... Valid values: 'abc', ...
@param num: a number
""",
MessageBase.STATE_DECLARED,

    MessageBase.NOTIFICATION, 
    "CATEGORY", "GROUP", "CODE", 
    "A string %s and a number %s are sent to the log")

