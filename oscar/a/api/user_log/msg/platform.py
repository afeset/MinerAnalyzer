
#
# Copyright Qwilt, 2013
#
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
#
# Author: shmulika
# 

from message_base import declareMessage, MessageBase
                
PowerOperationalStatusChanged = declareMessage(
"""
This message is created whenever the operational status of the power supplies changed
@version: 3.0.0.0
@format: Power operational-status changed to [new-status]
@param new-status: Valid values: 'up', 'degraded', 'unknown'
""", 
MessageBase.STATE_ACTIVE,

    MessageBase.ERROR, 
    "PLATFORM", "POWER", "OPERATIONAL-STATUS-CHANGED",
    "Power operational-status changed to %s")


PowerSupplyOperationalStatusChanged = declareMessage(
"""
This message is created whenever the operational status of the a power supply has changed
@version: 3.0.0.0
@format: Power supply [power-supply-entity] at location `[location]` operational-status changed to [new-status]
@param power-supply-entity: String
@param location: String
@param new-status: Valid values: 'up', 'down', 'unknown'
""", 
MessageBase.STATE_ACTIVE,

    MessageBase.ERROR, 
    "PLATFORM", "POWER", "POWER-SUPPLY-OPERATIONAL-STATUS-CHANGED",
    "Power supply %s at location '%s' operational-status changed to %s")


FansOperationalStatusChanged = declareMessage(
"""
This message is created whenever the operational status of the fans changed
@version: 3.0.0.0
@format: Fans operational-status changed to [new-status]
@param new-status: Valid values: 'up', 'degraded', 'down', 'unknown'
""", 
MessageBase.STATE_ACTIVE,

    MessageBase.ERROR, 
    "PLATFORM", "FANS", "OPERATIONAL-STATUS-CHANGED",
    "Fans operational-status changed to %s")


FanOperationalStatusChanged = declareMessage(
"""
This message is created whenever the operational status of the a fan has changed
@version: 3.0.0.0
@format: Fan [fan-entity] at location `[location]` operational-status changed to [new-status]
@param fan-entity: String
@param location: String
@param new-status: Valid values: 'up', 'down', 'unknown'
""", 
MessageBase.STATE_ACTIVE,

    MessageBase.ERROR, 
    "PLATFORM", "FANS", "FAN-OPERATIONAL-STATUS-CHANGED",
    "Fan %s at location '%s' operational-status changed to %s")


SystemTemperatureOperationalStatusChangedWarning = declareMessage(
"""
This message is created whenever the operational status of the system temperature has changed to or from warning
@version: 3.5.0.0
@format: System temperature operational-status changed to [new-status]
@param new-status: Valid values: 'ok', 'warning', 'unknown'
""", 
MessageBase.STATE_ACTIVE,

    MessageBase.WARNING, 
    "PLATFORM", "TEMPERATURE", "SYSTEM-OPERATIONAL-STATUS-CHANGED-WARNING",
    "System temperature operational-status changed to %s")


SystemTemperatureOperationalStatusChangedCritical = declareMessage(
"""
This message is created whenever the operational status of the system temperature has changed to or from critical
@version: 3.5.0.0
@format: System temperature operational-status changed to [new-status]
@param new-status: Valid values: 'ok', 'critical', 'unknown'
""", 
MessageBase.STATE_ACTIVE,

    MessageBase.CRITICAL, 
    "PLATFORM", "TEMPERATURE", "SYSTEM-OPERATIONAL-STATUS-CHANGED-CRITICAL",
    "System temperature operational-status changed to %s")


TemperatureSensorOperationalStatusChangedWarning = declareMessage(
"""
This message is created whenever the operational status of a temperature sensor has changed to or from warning
@version: 3.5.0.0
@format: Temperature sensor [sensor-entity] at location '[location]' operational-status changed to [new-status]. Temperature is [temperature]C. Warning range is outside [minimum-warning]C - [maximum-warning]C
@param sensor-entity: String
@param location: String
@param temperature: number
@param minimum-critical: number
@param maximum-critical: number
@param new-status: Valid values: 'ok', 'warning', 'unknown'
""", 
MessageBase.STATE_ACTIVE,

    MessageBase.WARNING, 
    "PLATFORM", "TEMPERATURE", "SENSOR-OPERATIONAL-STATUS-CHANGED-WARNING",
    "Temperature sensor %s at location '%s' operational-status changed to %s. Temperature is %sC. Warning range is outside %sC - %sC")


TemperatureSensorOperationalStatusChangedCritical = declareMessage(
"""
This message is created whenever the operational status of a temperature sensor has changed to or from critical
@version: 3.5.0.0
@format: Temperature sensor [sensor-entity] at location '[location]' operational-status changed to [new-status]. Temperature is [temperature]C. Critical range is outside [minimum-critical]C - [maximum-critical]C
@param sensor-entity: String
@param location: String
@param temperature: number
@param minimum-critical: number
@param maximum-critical: number
@param new-status: Valid values: 'ok', 'critical', 'unknown'
""", 
MessageBase.STATE_ACTIVE,

    MessageBase.CRITICAL, 
    "PLATFORM", "TEMPERATURE", "SENSOR-OPERATIONAL-STATUS-CHANGED-CRITICAL",
    "Temperature sensor %s at location '%s' operational-status changed to %s. Temperature is %sC. Critical range is outside %sC - %sC")


