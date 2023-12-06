import math

from subsystems.drivetrain import Drivetrain
from utils.safecommand import SafeCommand


class TournerX(SafeCommand):
    def __init__(self, drive: Drivetrain, angle: float, speed: float):
        super().__init__()
        self.angle = angle
        self.drive = drive
        self.speed = speed
        self.addRequirements(self.drive)
        self.error = float('inf')

    def initialize(self):
        self.drive.resetOdometry()

    def execute(self):
        self.error = self.drive.getAngle() - self.angle


    def isFinished(self) -> bool:
        return abs(self.error) <= 3