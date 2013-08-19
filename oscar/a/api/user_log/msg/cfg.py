#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: nirs
# 

from message_base import declareMessage, MessageBase
                

Configured = declareMessage(
"""
This message is created whenever a configuration is successfully submitted
@version: 
@format: Configured from [IP-address] by [user-name]
@param IP-address
@param user-name
""", 
MessageBase.STATE_DECLARED,

    MessageBase.NOTIFICATION, 
    "SYS", "CFG", "CONFIG_I",
    "Configured from %s by %s")


SshLogin = declareMessage(
"""
This message is created upon a successful user Login to CLI
@version: 
@format: Login success user [user-name] from [IP-address]
@param user-name
@param IP-address
""",
MessageBase.STATE_DECLARED,

    MessageBase.NOTIFICATION, 
    "SECURITY", "SSHD", "LOGIN_SUCCESS", 
    "Login success user %s from %s")


SshLoginFailure = declareMessage(
"""
This message is created upon a failure of user Login to CLI
@version: 
@format: Login failure user [user-name] from [IP-address]. Reason: [reason]
@param user-name
@param IP-address
@param reason: Valid values: 'bad password'
""",
MessageBase.STATE_DECLARED,

    MessageBase.NOTIFICATION, 
    "SECURITY", "SSHD", "LOGIN_FAILURE", 
    "Login failure user %s from %s. Reason: %s")


SshLogout = declareMessage(
"""
This message is created upon a user Logout from the CLI
@version: 
@format: Logout user [user-name] from [IP-address]. Reason: [reason]
@param user-name
@param IP-address
@param reason: Valid values: 'user logout', 'session disconnect', 'session timeout', 'unknown'
""",
MessageBase.STATE_DECLARED,

    MessageBase.INFORMATIONAL, 
    "SECURITY", "SSHD", "LOGOUT", 
    "Logout user %s from %s. Reason: %s")

