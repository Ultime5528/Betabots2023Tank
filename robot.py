#!/usr/bin/env python3
from typing import Optional

import commands2
import wpilib
from commands2.button import CommandXboxController

from commands.autonomous.autourgence import AutoUrgence
from commands.autonomous.avancerx import AvancerX
from commands.autonomous.tournerx import TournerX
from commands.autonomous.urgence import BougerUrgence
from commands.drive import Drive
from commands.extend import ExtendStrong
from commands.launch import Launch
from commands.movearm import MoveArm
from commands.resetarm import ResetProtocol
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
        self.stick = commands2.button.CommandJoystick(1)

        self.arm = Arm()
        self.launcher = Launcher()
        self.drivetrain = Drivetrain()
        self.drivetrain.setDefaultCommand(Drive(self.drivetrain, self.xboxremote))

        self.autoChooser = wpilib.SendableChooser()
        self.autoCommand: Optional[commands2.CommandBase] = None

        self.autoChooser.addOption("AutoBasic", BougerUrgence(self.drivetrain, 0.5, 1.2, 0))

        wpilib.SmartDashboard.putData("AvancerX", AvancerX(self.drivetrain, 0.5, 0.75))
        wpilib.SmartDashboard.putData("TournerX", TournerX(self.drivetrain, 0.5, 0.75))
        wpilib.SmartDashboard.putData("ExtendStrong", ExtendStrong(self.launcher))

        self.setupButtons()

    #copilote

    def setupButtons(self):
        self.stick.button(1).onTrue(Launch(self.launcher))
        #self.xboxremote.button(1).onTrue(BougerUrgence(self.drivetrain, 0.4, 1.2, 0.5))
        #self.stick.button(8).onTrue(ResetProtocol(self.arm))
        #self.stick.button(5).onTrue(MoveArm.toLevel1(self.arm))
        #self.stick.button(3).onTrue(MoveArm.toLevel2(self.arm))
        #self.stick.button(4).onTrue(MoveArm.toLevel3(self.arm))


    def autonomousInit(self) -> None:
        self.autoCommand: commands2.CommandBase = self.autoChooser.getSelected()
        if self.autoCommand:
            self.autoCommand.schedule()

    def teleopInit(self) -> None:
        if self.autoCommand:
            self.autoCommand.cancel()

    def setupDashboard(self):

        self.autoCommand = None
        self.autoChooser.addOption("atterissage", BougerUrgence(self.drivetrain, 0.5, 1.2, 0))
        self.autoChooser.addOption("autoComplet", AutoUrgence(self.drivetrain, self.launcher))
            


if __name__ == "__main__":
    wpilib.run(Robot)
