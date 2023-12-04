#!/usr/bin/env python3
import math
from typing import Optional
import commands2
import wpilib
from commands2._impl.button import JoystickButton

from commands.resetarm import ResetArm
from commands.movearm import MoveArm
from subsystems.arm import Arm


class Robot(commands2.TimedCommandRobot):
    def robotInit(self):
        #self.stick = commands2.button.CommandJoystick(0)
        self.autoChooser = wpilib.SendableChooser()
        self.autoCommand: Optional[commands2.CommandBase] = None

        self.arm = Arm()
        self.stick = wpilib.Joystick(0)
        JoystickButton(self.stick, 1).whenPressed(MoveArm.toLevel1(self.arm))
        JoystickButton(self.stick, 3).whenPressed(MoveArm.toLevel2(self.arm))
        JoystickButton(self.stick, 2).whenPressed(ResetArm(self.arm))


    def autonomousInit(self) -> None:
        self.autoCommand: commands2.CommandBase = self.autoChooser.getSelected()
        if self.autoCommand:
            self.autoCommand.schedule()

    def teleopInit(self) -> None:
        if self.autoCommand:
            self.autoCommand.cancel()


if __name__ == "__main__":
    wpilib.run(Robot)
