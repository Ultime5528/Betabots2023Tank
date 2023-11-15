#!/usr/bin/env python3
import math
from typing import Optional

import commands2
import wpilib
from commands2._impl.button import CommandJoystick

from commands.drive import Drive
from subsystems.drivetrain import Drivetrain


class Robot(commands2.TimedCommandRobot):
    def __init__(self):
        super().__init__()
        self.stick = CommandJoystick(0)
        self.drivetrain = Drivetrain()

        self.drivetrain.setDefaultCommand(Drive(self.drivetrain, self.stick))



if __name__ == "__main__":
    wpilib.run(Robot)
