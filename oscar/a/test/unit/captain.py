#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

#This class holds the captain basic global functionality to allow captain to exists in UTs

import sys
import os
import traceback
import a.api.user_log.msg.message_base
import a.infra.process.captain

class Captain(a.infra.process.captain.Captain):
    def __init__ (self, logger): 
        a.infra.process.captain.Captain.__init__(self)
        self._log = logger.createLogger("ut", "captain")

    def getKickNumber (self):
        return 0

    def logUserMessage (self, userLogMessage):
        """create a user log message
        """
        (isValid, msgText) = self._verifyUserMessage(userLogMessage)
        if not isValid:
            return

        self._log("no-user-log-service-support").notice("trying to log user message:  %s-%s-%s-%s: %s",
                                                        userLogMessage.category, userLogMessage.group, userLogMessage.severity, 
                                                        userLogMessage.code, msgText)


