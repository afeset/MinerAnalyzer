#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

from message_base import declareMessage, MessageBase
                
LinkUpDown = declareMessage(
"""
This message is created upon network interface state change
@version: 2.6.0.0
@format: Interface [interface], changed state to [state]
@param interface
@param state: Valid values: 'down' (initial state), 'up', 'administratively down', 'unknown'
""",
MessageBase.STATE_ACTIVE,

    MessageBase.NOTIFICATION, 
    "NET", "LINK", "UPDOWN",
    "Interface %s, changed state to %s")


ConnectivityTestChange = declareMessage(
"""
This message is created upon network connectivity check result change
@version: 2.6.0.0
@format: Interface [interface] [protocol] connectivity check operational state changed to [state]. Reason: [reason]
@param interface
@param protocol: Valid values: 'IPv4', 'IPv6'
@param state: Valid values: 'down' (initial state), 'up', 'not applicable', 'unknown'
@param reason: TBD
""",
MessageBase.STATE_ACTIVE,

    MessageBase.NOTIFICATION, 
    "NET", "CONNECTIVITY-CHECK", "CHANGE",
    "Interface %s %s connectivity check operational state changed to %s. Reason: %s")


ClearCounter = declareMessage(
"""
This message is created upon clearing of network interface counters
@version: 2.6.0.0
@format: Interface [interface] counters were cleared
@param interface
""",
MessageBase.STATE_ACTIVE,

    MessageBase.INFORMATIONAL, 
    "NET", "INTERFACE", "CLEAR_COUNTERS",
    "Interface %s counters were cleared")



