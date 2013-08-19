#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

from message_base import declareMessage, MessageBase
                
ContentDiskState = declareMessage(
"""
This message is created whenever a content disk state is changed
@version: 2.6.0.0
@format: Content disk [disk-name], changed state to [state]. Reason: [reason]
@param disk-name
@param state: Valid values: 'up' (initial state), 'down', 'disabled' (future)
@param reason: Valid values: 'disk was initialized', 'absent', 'disk error', 'foreign'
""", 
MessageBase.STATE_ACTIVE,

    MessageBase.NOTIFICATION, 
    "CONTENT", "DISK", "CHANGE",
    "Content disk %s, changed state to %s. Reason: %s")


ContentDiskInit = declareMessage(
"""
This message is created whenever a content disk was initialized
@version: 2.6.0.0
@format: Content disk [disk-name] was initialized
@param disk-name
""", 
MessageBase.STATE_ACTIVE,

    MessageBase.NOTIFICATION, 
    "CONTENT", "DISK", "INIT",
    "Content disk %s was initialized")


ContentDiskCount = declareMessage(
"""
This message is created upon application start
@version: 2.6.0.0
@format: [num-active-content-disks] of [num-configured-content-disks] content disks are in up state. [min-disk-count] are required for acquisition and delivery.
@param num-active-content-disks
@param num-configured-content-disks
@param min-disk-count
""", 
MessageBase.STATE_ACTIVE,

    MessageBase.NOTIFICATION, 
    "CONTENT", "DISK", "UP_COUNT",
    "%s of %s content disks are in up state. %s are required for acquisition and delivery.")


ContentDiskLowCount = declareMessage(
"""
@version: 2.6.0.0
@format: Not enough content disk in up state. Only [num-active-content-disks] out of [num-configured-content-disks] content disks are in up state. [min-disk-count] are required for acquisition and delivery.
@param num-active-content-disks
@param num-configured-content-disks
@param min-disk-count
""", 
MessageBase.STATE_ACTIVE,

    MessageBase.CRITICAL, 
    "CONTENT", "DISK", "TOO_LOW_UP_COUNT",
    "Not enough content disk in up state. Only %s out of %s content disks are in up state. %s are required for acquisition and delivery.")


