#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

class MessageBase(object):
    EMERGENCY = 0
    ALERT = 1
    CRITICAL = 2
    ERROR = 3
    WARNING = 4
    NOTIFICATION = 5
    INFORMATIONAL = 6
    DEBUGGING = 7

    STATE_DECLARED = 0
    STATE_ACTIVE   = 1

    ourMessages = []

    def __init__ (self, state, severity, category, group, code, devComment, text, *args):
        self.state      = state
        self.severity   = severity
        self.category   = category
        self.group      = group
        self.code       = code
        self.devComment = devComment
        self.text       = text
        self.args       = args

    def getStateStr (self):
        stateNames = {self.STATE_DECLARED: "declared",
                      self.STATE_ACTIVE:   "active"}
        if self.state not in stateNames:
            return 'unknown'
        return stateNames[self.state]

    def getIsActive (self):
        activeStates = [self.STATE_ACTIVE]
        return self.state in activeStates

    @classmethod
    def s_getMessagesList (cls):
        return cls.ourMessages

    @classmethod
    def s_clearMessagesList (cls):
        cls.ourMessages = []

    @classmethod
    def s_addMessagesToList (cls, msg):
        return cls.ourMessages.append(msg)
        
                
def declareMessage (devComment, state, severity, category, group, code, text):    
    def messageCreator (*args):
        return MessageBase(state, severity, category, group, code, devComment, text, *args)
    MessageBase.s_addMessagesToList(messageCreator())
    return messageCreator


