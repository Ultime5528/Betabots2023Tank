#!/usr/bin/env python3
import math
from typing import Optional
import commands2
import wpilib
from commands2._impl.button import CommandJoystick, CommandXboxController

from commands.avancerx import AvancerX
from commands.drive import Drive
from commands.launch import Launch
from commands.movearm import MoveArm
from commands.resetarm import ResetArm
from subsystems.drivetrain import Drivetrain


class Robot(commands2.TimedCommandRobot):
    def __init__(self):
        super().__init__()
        self.xboxremote = CommandXboxController(0)
        
        self.drivetrain = Drivetrain()
        self.drivetrain.setDefaultCommand(Drive(self.drivetrain, self.xboxremote))
        
        self.autoChooser = wpilib.SendableChooser()
        self.autoCommand: Optional[commands2.CommandBase] = None

        wpilib.SmartDashboard.putData("AvancerX", AvancerX(self.drivetrain, 0.5, 0.75))


    def setupButtons(self):
        self.xboxremote.button(10).onTrue(Launch(self.lauch))
        self.xboxremote.button(4).onTrue(MoveArm(self.tolevel2))
        self.xboxremote.button(1).onTrue(ResetArm(self.resetarm))
        self.xboxremote.button(2).onTrue(MoveArm(self.tolevel1))
    def autonomousInit(self) -> None:
        self.autoCommand: commands2.CommandBase = self.autoChooser.getSelected()
        if self.autoCommand:
            self.autoCommand.schedule()

    def teleopInit(self) -> None:
        if self.autoCommand:
            self.autoCommand.cancel()


if __name__ == "__main__":
    wpilib.run(Robot)
