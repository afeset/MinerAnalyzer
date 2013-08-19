#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

from message_base import declareMessage, MessageBase
                

AppUserRestart = declareMessage(
"""
This message is created when user is initiating an application restart
@version: 2.6.0.0
@format: User initiated application restart. Reason: [reason], application started at [date]
@param reason: Application restart reason. Valid values: 'user command', 'technician', 'unknown', 'software upgrade', 'software downgrade'
@param date: Application last start time
""",
MessageBase.STATE_ACTIVE,

    MessageBase.NOTIFICATION, 
    "SYS", "SYSMGR", "USER_APP_RESTART", 
    "User initiated application restart. Reason: %s, application started at %s")

OsUserRestart = declareMessage(
"""
This message is created when user is initiating an OS restart
@version: 2.6.0.0
@format: User initiated OS restart. Reason: [reason], OS started at [date]
@param reason: Os restart reason. Valid values: 'user command', 'technician', 'unknown', 'software upgrade', 'software downgrade'
@param date: OS last start time
""",
MessageBase.STATE_ACTIVE,

    MessageBase.NOTIFICATION, 
    "SYS", "SYSMGR", "USER_OS_RESTART", 
    "User initiated OS restart. Reason: %s, OS started at %s")


AppAbnornalRestart = declareMessage(
"""
This message is created when an application restart is called automatically
@version: 2.6.0.0
@format:  Abnormal application restart. Reason: [reason], application started at [date]
@param reason: Application restart reason. Valid values: 'application failure'
@param date: Application last start time
""",
MessageBase.STATE_ACTIVE,

    MessageBase.ERROR, 
    "SYS", "SYSMGR", "ABNORMAL_APP_RESTART", 
    "Abnormal application restart. Reason: %s, application started at %s")


OsAbnornalRestart = declareMessage(
"""
This message is created when an OS restart is called automatically
@version: 2.6.0.0
@format:  Abnormal OS restart. Reason: [reason], OS started at [date]
@param reason: OS restart reason. Valid values: 'OS failure', 'OS problem', 'content disk problem'
@param date: OS last start time
""",
MessageBase.STATE_ACTIVE,

    MessageBase.ALERT, 
    "SYS", "SYSMGR", "ABNORMAL_OS_RESTART", 
    "Abnormal OS restart. Reason: %s, OS started at %s")


AppUserShutdown = declareMessage(
"""
This message is created when user is initiating an application shutdown
@version: 2.6.0.0
@format: User initiated application shutdown. Reason: [reason], application started at [date]
@param reason: Application shutdown reason. Valid values: 'user command', 'technician', 'unknown'
@param date: Application last start time
""",
MessageBase.STATE_ACTIVE,

    MessageBase.WARNING, 
    "SYS", "SYSMGR", "USER_APP_SHUTDOWN", 
    "User initiated application shutdown. Reason: %s, application started at %s")


OsUserShutdown = declareMessage(
"""
This message is created when user is initiating an OS shutdown
@version: 2.6.0.0
@format: User initiated OS shutdown. Reason: [reason], OS started at [date]
@param reason: Os shutdown reason. Valid values: 'user command', 'technician', 'unknown'
@param date: OS last start time
""",
MessageBase.STATE_ACTIVE,

    MessageBase.WARNING, 
    "SYS", "SYSMGR", "USER_OS_SHUTDOWN", 
    "User initiated OS shutdown. Reason: %s, OS started at %s")

UserPowerOff = declareMessage(
"""
This message is created when user is initiating a power-off sequence
@version: 2.6.0.0
@format: User initiated power-off sequence. Reason: [reason], OS started at [date]
@param reason: Valid values: 'user command', 'technician', 'unknown'
@param date: OS last start time
""",
MessageBase.STATE_ACTIVE,

    MessageBase.WARNING,
    "SYS", "SYSMGR", "USER_POWER_OFF",
    "User initiated power-off sequence. Reason: %s, OS started at %s")

AppAbnormalShutdown = declareMessage(
"""
This message is created when an application shutdown is called automatically
@version: 2.6.0.0
@format: Abnormal application shutdown. Reason: [reason], application started at [date]
@param reason: Application shutdown reason. Valid values: 'persistent application failure'
@param date: Application last start time
""",
MessageBase.STATE_ACTIVE,

    MessageBase.ALERT, 
    "SYS", "SYSMGR", "ABNORMAL_APP_SHUTDOWN", 
    "Abnormal application shutdown. Reason: %s, application started at %s")


OsAbnormalShutdown = declareMessage(
"""
This message is created when an OS shutdown is called automatically
@version: 
@format: Abnormal OS shutdown. Reason: [reason], OS started at [date]
@param reason: OS shutdown reason. Valid values: 'persistent OS failure'
@param date: OS last start time
""",
MessageBase.STATE_DECLARED,

    MessageBase.CRITICAL, 
    "SYS", "SYSMGR", "ABNORMAL_OS_SHUTDOWN", 
    "Abnormal OS shutdown. Reason: %s, OS started at %s")

AppColdStart = declareMessage(
"""
This message is created when the application is started
@version: 2.6.0.0
@format: Application cold start version [version]
@param version: Application version
""",
MessageBase.STATE_ACTIVE,

    MessageBase.NOTIFICATION, 
    "SYS", "SYSMGR", "APP_COLDSTART", 
    "Application cold start version %s")


OsColdStart = declareMessage(
"""
This message is created when the OS is started
@version: 2.6.0.0
@format: OS cold start version [version]
@param version: OS version
""",
MessageBase.STATE_ACTIVE,

    MessageBase.NOTIFICATION, 
    "SYS", "SYSMGR", "OS_COLDSTART", 
    "OS cold start version %s")


AppUnexpectedStart = declareMessage(
"""
This message is created when an application start is called without proper shutdown
@version: 2.6.0.0
@format: Application was not properly shutdown prior to this start
""",
MessageBase.STATE_ACTIVE,

    MessageBase.WARNING, 
    "SYS", "SYSMGR", "UNEXPECTED_APP_START", 
    "Application was not properly shutdown prior to this start")

OsUnexpectedStart = declareMessage(
"""
This message is created when an OS start is called without proper shutdown
@version: 2.6.0.0
@format: OS was not properly shutdown prior to this start
""",
MessageBase.STATE_ACTIVE,

    MessageBase.WARNING, 
    "SYS", "SYSMGR", "UNEXPECTED_OS_START", 
    "OS was not properly shutdown prior to this start")

ClearUserLog = declareMessage(
"""
This message is created when the events log is cleared
@version: 2.6.0.0
@format: Events log was cleared
""",
MessageBase.STATE_ACTIVE,

    MessageBase.INFORMATIONAL, 
    "SYS", "EVENTS", "CLEAR_LOG", 
    "Events log was cleared")


ClearAuditLog = declareMessage(
"""
This message is created when the audit log is cleared
@version: 2.6.0.0
@format: Audit log was cleared
""",
MessageBase.STATE_ACTIVE,

    MessageBase.INFORMATIONAL, 
    "SYS", "AUDIT", "CLEAR_LOG", 
    "Audit log was cleared")



