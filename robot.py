#!/usr/bin/env python3
import math
from typing import Optional
import commands2
import wpilib
from commands2._impl.button import CommandXboxController

from commands.avancerx import AvancerX
from commands.drive import Drive
from commands.extend import ExtendStrong, ExtendWeak
from commands.launch import Launch
from commands.movearm import MoveArm
from commands.resetarm import ResetArm
from subsystems.arm import Arm
from subsystems.launcher import Launcher
from subsystems.drivetrain import Drivetrain


class Robot(commands2.TimedCommandRobot):
    def __init__(self):
        super().__init__()
        self.xboxremote = CommandXboxController(0)
        self.launcher = Launcher()
        self.drivetrain = Drivetrain()
        self.drivetrain.setDefaultCommand(Drive(self.drivetrain, self.xboxremote))
        self.autoChooser = wpilib.SendableChooser()
        self.autoCommand: Optional[commands2.CommandBase] = None

        self.arm = Arm()
        JoystickButton(self.stick, 1).whenPressed(MoveArm.toLevel1(self.arm))
        JoystickButton(self.stick, 3).whenPressed(MoveArm.toLevel2(self.arm))
        JoystickButton(self.stick, 2).whenPressed(ResetArm(self.arm))
        wpilib.SmartDashboard.putData("ExtendStrong", ExtendStrong(self.launcher))
        wpilib.SmartDashboard.putData("ExtendWeak", ExtendWeak(self.launcher))
        self.setupButtons()

        wpilib.SmartDashboard.putData("AvancerX", AvancerX(self.drivetrain, 0.5, 0.75))

    def setupButtons(self):
        self.xboxremote.button(10).onTrue(Launch(self.launcher))
        self.xboxremote.button(4).onTrue(MoveArm.toLevel2(self.arm))
        self.xboxremote.button(1).onTrue(ResetArm(self.arm))
        self.xboxremote.button(2).onTrue(MoveArm.toLevel1(self.arm))

    def autonomousInit(self) -> None:
        self.autoCommand: commands2.CommandBase = self.autoChooser.getSelected()
        if self.autoCommand:
            self.autoCommand.schedule()

    def teleopInit(self) -> None:
        if self.autoCommand:
            self.autoCommand.cancel()


if __name__ == "__main__":
    wpilib.run(Robot)
