
#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

from message_base import declareMessage, MessageBase
                

OsUpgrade = declareMessage(
"""
This message is created upon os upgrade
@version: 2.6.0.0
@format: Upgrading OS from version [current-version] to version [next-version]
@param current-version
@param next-version
""",
MessageBase.STATE_ACTIVE,

    MessageBase.NOTIFICATION, 
    "SYS", "INSTALL", "OS_UPGRADE", 
    "Upgrading OS from version %s to version %s")

OsDowngrade = declareMessage(
"""
This message is created upon os downgrade
@version: 2.6.0.0
@format: Downgrading OS from version [current-version] down to version [next-version]
@param current-version
@param next-version
""",
MessageBase.STATE_ACTIVE,

    MessageBase.NOTIFICATION, 
    "SYS", "INSTALL", "OS_DOWNGRADE", 
    "Downgrading OS from version %s down to version %s")



AppUpgrade = declareMessage(
"""
This message is created upon application upgrade
@version: 2.6.0.0
@format: Upgrading application from version [current-version] to version [next-version]
@param current-version
@param next-version
""",
MessageBase.STATE_ACTIVE,

    MessageBase.NOTIFICATION, 
    "SYS", "INSTALL", "APP_UPGRADE", 
    "Upgrading application from version %s to version %s")

AppDowngrade = declareMessage(
"""
This message is created upon application downgrade
@version: 2.6.0.0
@format: Downgrading application from version [current-version] down to version [next-version]
@param current-version
@param next-version
""",
MessageBase.STATE_ACTIVE,

    MessageBase.NOTIFICATION, 
    "SYS", "INSTALL", "APP_DOWNGRADE", 
    "Downgrading application from version %s down to version %s")


MspUpgrade = declareMessage(
"""
This message is created upon MSP (Media Support Package) upgrade
@version: 2.6.0.0
@format: MSP (Media Signature Package) upgraded from version [current-msp-version] to version [next-msp-version]
@param current-msp-version
@param next-msp-version
""",
MessageBase.STATE_ACTIVE,

    MessageBase.NOTIFICATION, 
    "SYS", "INSTALL", "MSP_UPGRADE", 
    "MSP (Media Signature Package) upgraded from version %s to version %s")

MspDowngrade = declareMessage(
"""
This message is created upon MSP (Media Support Package) downgrade
@version: 2.6.0.0
@format: MSP (Media Signature Package) downgraded from version [current-msp-version] down to version [next-msp-version]
@param current-msp-version
@param next-msp-version
""",
MessageBase.STATE_ACTIVE,

    MessageBase.NOTIFICATION, 
    "SYS", "INSTALL", "MSP_DOWNGRADE", 
    "MSP (Media Signature Package) downgraded from version %s down to version %s")



