#!/usr/bin/env python3
import math
from typing import Optional
import commands2
import wpilib

from commands.extend import ExtendStrong, ExtendWeak
from subsystems.launcher import Launcher


class Robot(commands2.TimedCommandRobot):
    def __init__(self):
        super().__init__()

        #self.stick = commands2.button.CommandJoystick(0)
        self.autoChooser = wpilib.SendableChooser()
        self.autoCommand: Optional[commands2.CommandBase] = None

        self.launcher = Launcher()

        wpilib.SmartDashboard.putData("ExtendStrong", ExtendStrong(self.launcher))
        wpilib.SmartDashboard.putData("ExtendWeak", ExtendWeak(self.launcher))

    def autonomousInit(self) -> None:
        self.autoCommand: commands2.CommandBase = self.autoChooser.getSelected()
        if self.autoCommand:
            self.autoCommand.schedule()

    def teleopInit(self) -> None:
        if self.autoCommand:
            self.autoCommand.cancel()


if __name__ == "__main__":
    wpilib.run(Robot)
