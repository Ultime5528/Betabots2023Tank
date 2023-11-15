import wpilib
import commands2.button

from subsystems import drivetrain
from subsystems.drivetrain import Drivetrain
from utils.safecommand import SafeCommand


class Drive(SafeCommand):
    def __init__(self, drivetrain: Drivetrain, stick: wpilib.Joystick):
        super().__init__()
        self.stick = stick
        self.drivetrain = drivetrain
        self.addRequirements(drivetrain)

    def execute(self):
        self.drivetrain.drive(self.stick.getY() * -1, self.stick.getX() * -1)

    def end(self, interrupted: bool) -> None:
        self.drivetrain.drive(0.0, 0.0)
