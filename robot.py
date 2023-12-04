#!/usr/bin/env python3
import math

from typing import Optional
import commands2
import wpilib
from commands2.button import CommandXboxController

from commands.drive import Drive
from commands.launch import Launch
from subsystems.drivetrain import Drivetrain
from subsystems.launcher import Launcher


class Robot(commands2.TimedCommandRobot):
    def __init__(self):
        super().__init__()
        self.xboxremote = CommandXboxController(0)
        
        self.drivetrain = Drivetrain()
        self.drivetrain.setDefaultCommand(Drive(self.drivetrain, self.xboxremote))
        
        self.autoChooser = wpilib.SendableChooser()
        self.autoCommand: Optional[commands2.CommandBase] = None

    def setupButtons(self):
        self.xboxremote.button(10).onTrue(Launch(self.lauch))
        self.xboxremote.button(4).onTrue(#monter)
        self.xboxremote.button(1).onTrue(#zéro)
        self.xboxremote.button(2).onTrue(#millieu)

    def autonomousInit(self) -> None:
        self.autoCommand: commands2.CommandBase = self.autoChooser.getSelected()
        if self.autoCommand:
            self.autoCommand.schedule()

    def teleopInit(self) -> None:
        if self.autoCommand:
            self.autoCommand.cancel()


if __name__ == "__main__":
    wpilib.run(Robot)
