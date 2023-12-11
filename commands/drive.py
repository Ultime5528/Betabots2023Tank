import wpilib
import commands2.button

from subsystems import drivetrain
from subsystems.drivetrain import Drivetrain
from utils.safecommand import SafeCommand


class Drive(SafeCommand):
    def __init__(self, drivetrain: Drivetrain, xboxremote: wpilib.XboxController):
        super().__init__()
        self.xboxremote = xboxremote
        self.drivetrain = drivetrain
        self.addRequirements(drivetrain)

    def execute(self):
        self.drivetrain.drive(self.xboxremote.getLeftY() * -1, self.xboxremote.getLeftX() * -1)

    def end(self, interrupted: bool) -> None:
        self.drivetrain.drive(0.0, 0.0)
