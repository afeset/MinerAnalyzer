
#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

from message_base import declareMessage, MessageBase
                
DeliveryStateChange = declareMessage(
"""
This message is created upon delivery state change
@version: 2.6.0.0
@format: Content delivery state changed to [state]. Reason: [reason]
@param state: Valid values: 'enabled' (default), 'disabled'
@param reason: Valid values: 'not enough content disks in up state', 'no available delivery interface'
""",
MessageBase.STATE_ACTIVE,

    MessageBase.CRITICAL, 
    "CONTENT", "DELIVERY", "CHANGE", 
    "Content delivery state changed to %s. Reason: %s")


DeliveryInterfaceIpv4Request = declareMessage(
"""
This message is created upon change in the actual delivery interface
@version: 2.6.0.0
@format: Interface [analytic-interface] IPv4 content requests are delivered by [i/f-list]
@param analytic-interface
@param i/f-list: note: currently i/f list is one or none (if all are down).
""",
MessageBase.STATE_ACTIVE,

    MessageBase.NOTIFICATION, 
    "CONTENT", "DELIVERY", "IPV4_REQUEST_INTERFACE", 
    "Interface %s IPv4 content requests are delivered by %s")

#this message is used by c++ code. it is declared in the python content module for auto documentation (till available for c++)
DeliveryInterfaceIpv6Request = declareMessage(
"""
This message is created upon change in the actual delivery interface
@version: 2.7.0.0
@format: Interface [analytic-interface] IPv6 content requests are delivered by [i/f-list]
@param analytic-interface
@param i/f-list: note: currently i/f list is one or none (if all are down).
""",
MessageBase.STATE_ACTIVE,

    MessageBase.NOTIFICATION, 
    "CONTENT", "DELIVERY", "IPV6_REQUEST_INTERFACE", 
    "Interface %s IPv6 content requests are delivered by %s")


AcquisitionStateChange = declareMessage(
"""
This message is created upon acquisition state change
@version: 
@format: Content acquisition state changed to [state]. Reason: [reason]
@param state: Valid values: 'enabled' (default), 'disabled'
@param reason: Valid values: 'not enough content disks in up state'
""",
MessageBase.STATE_DECLARED,

    MessageBase.ERROR, 
    "CONTENT", "ACQUISITION", "CHANGE", 
    "Content acquisition state changed to %s. Reason: %s")


