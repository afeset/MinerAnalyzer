#
# Copyright Qwilt, 2011
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: amiry
# 

from message_base import declareMessage, MessageBase
                
QueueGettingFull = declareMessage(
"""
This message is created when content reporting export queue is gettign full
@version: 3.0.0.0
@format: [export-name] reports queue state is [state]
@param export-name: name of the export
@param state: can be "getting-full" or "normal"
""",
MessageBase.STATE_ACTIVE,

    MessageBase.WARNING, 
    "CONTENT", "EXPORT", "QUEUE_GETTING_FULL",
    "%s reports queue state is %s")

QueueFull = declareMessage(
"""
This message is created when content reporting export queue is full
@version: 3.0.0.0
@format: [export-name] reports queue is full. [num-transations-lost] transactions lost
@param export-name: name of the export
@param num-transactions-lost: number of disacarded transactions
""",
MessageBase.STATE_ACTIVE,

    MessageBase.ERROR, 
    "CONTENT", "EXPORT", "QUEUE_FULL",
    "%s reports queue is full. %d transactions lost")

