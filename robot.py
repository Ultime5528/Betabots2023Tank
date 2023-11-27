#!/usr/bin/env python3
import math
from typing import Optional

import commands2
import wpilib
from commands2._impl.button import CommandJoystick, CommandXboxController

from commands.drive import Drive
from subsystems.drivetrain import Drivetrain


class Robot(commands2.TimedCommandRobot):
    def __init__(self):
        super().__init__()
        self.xboxremote = CommandXboxController(0)
        #self.stick = CommandJoystick(1)
        self.drivetrain = Drivetrain()

        # self.drivetrain.setDefaultCommand(Drive(self.drivetrain, self.stick))  # À commenter si on veut la manette.
        self.drivetrain.setDefaultCommand(Drive(self.drivetrain, self.xboxremote))  # À commenter si on veut le joystick.



if __name__ == "__main__":
    wpilib.run(Robot)
