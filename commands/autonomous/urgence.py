import wpilib

from utils.property import autoproperty
from utils.safecommand import SafeCommand
from subsystems.drivetrain import Drivetrain


class BougerUrgence(SafeCommand):

    def __init__(self, drivetrain: Drivetrain, speed: float, duration: float, rotation: float):
        super().__init__()
        self.drivetrain = drivetrain
        self.speed = speed
        self.duration = duration
        self.rotation = rotation
        self.timer = wpilib.Timer()
        self.addRequirements(self.drivetrain)

    def initialize(self) -> None:
        self.timer.reset()
        self.timer.start()

    def execute(self) -> None:
        self.drivetrain.drive(self.speed, self.rotation)

    def isFinished(self) -> bool:
        return self.timer.get() >= self.duration

    def end(self, interrupted: bool) -> None:
        self.drivetrain.drive(0, 0)

