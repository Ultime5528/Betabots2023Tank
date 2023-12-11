#!/usr/bin/env python3
from typing import Optional

import commands2
import wpilib
from commands2.button import CommandXboxController

from commands.drive import Drive
from commands.extend import ExtendStrong, ExtendWeak
from commands.launch import Launch
from commands.movearm import MoveArm
from commands.resetarm import ResetArm
from subsystems.arm import Arm
from subsystems.drivetrain import Drivetrain
from subsystems.launcher import Launcher


class Robot(commands2.TimedCommandRobot):
    def __init__(self):
        super().__init__()
        wpilib.LiveWindow.enableAllTelemetry()
        wpilib.LiveWindow.setEnabled(True)
        wpilib.DriverStation.silenceJoystickConnectionWarning(True)

        self.xboxremote = CommandXboxController(0)

        self.arm = Arm()
        self.launcher = Launcher()
        self.drivetrain = Drivetrain()
        self.drivetrain.setDefaultCommand(Drive(self.drivetrain, self.xboxremote))

        self.autoChooser = wpilib.SendableChooser()
        self.autoCommand: Optional[commands2.CommandBase] = None

        wpilib.SmartDashboard.putData("ExtendStrong", ExtendStrong(self.launcher))
        wpilib.SmartDashboard.putData("ExtendWeak", ExtendWeak(self.launcher))

        self.setupButtons()

    def setupButtons(self):
        self.xboxremote.button(6).onTrue(Launch(self.launcher))
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
