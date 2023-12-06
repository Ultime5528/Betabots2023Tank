#!/usr/bin/env python3
from typing import Optional
import commands2
import wpilib
from commands2._impl.button import CommandXboxController

from commands.autonomous.avancerx import AvancerX
from commands.drive import Drive
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
        
    def autonomousInit(self) -> None:
        self.autoCommand: commands2.CommandBase = self.autoChooser.getSelected()
        if self.autoCommand:
            self.autoCommand.schedule()

    def teleopInit(self) -> None:
        if self.autoCommand:
            self.autoCommand.cancel()


if __name__ == "__main__":
    wpilib.run(Robot)
