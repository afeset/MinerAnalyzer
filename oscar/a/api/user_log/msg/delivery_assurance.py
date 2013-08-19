#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

from message_base import declareMessage, MessageBase
                
TableClear = declareMessage(
"""
This message is created upon delivery assurance table clear
@version: 
@format: TBD
""",
MessageBase.STATE_DECLARED,

    MessageBase.INFORMATIONAL, 
    "CONTENT", "DELIVERY-ASSURANCE", "TBD-TABLE-CLEARED-TBD",
    "TBD")

