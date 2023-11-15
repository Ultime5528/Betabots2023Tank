#!/usr/bin/env python3
import math
from typing import Optional

import commands2
import wpilib
from commands2._impl.button import JoystickButton

from commands.Inclinatorzero import MoveToZero
from subsystems.inclinator import Inclinator




class Robot(commands2.TimedCommandRobot):
    def robotInit(self):
        #self.stick = commands2.button.CommandJoystick(0)
        self.autoChooser = wpilib.SendableChooser()
        self.autoCommand: Optional[commands2.CommandBase] = None

        self.inclinator = Inclinator()
        self.stick = wpilib.Joystick(0)

    def autonomousInit(self) -> None:
        self.autoCommand: commands2.CommandBase = self.autoChooser.getSelected()
        if self.autoCommand:
            self.autoCommand.schedule()

    def teleopInit(self) -> None:
        if self.autoCommand:
            self.autoCommand.cancel()

    def robotPeriodic(self) -> None:
        super().robotPeriodic()


if __name__ == "__main__":
    wpilib.run(Robot)
