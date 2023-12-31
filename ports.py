from typing import Final

"""
Respect the naming convention : "subsystem" _ "component type" _ "precision"

Put port variables into the right category: CAN - PWM - DIO

Order port numbers, ex:
    drivetrain_motor_fl: Final = 0
    drivetrain_motor_fr: Final = 1
    drivetrain_motor_rr: Final = 2
"""

# CAN
arm_motor = 5

# PWM

# DIO
arm_limitswitch = 0

# PCM
launcher_piston_strong_backwards = 2
launcher_piston_strong_forward = 3
