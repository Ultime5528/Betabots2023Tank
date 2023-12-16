import wpilib
from utils.safecommand import SafeCommand
from subsystems.launcher import Launcher
from utils.property import autoproperty


class ExtendStrong(SafeCommand):
    duration = autoproperty(0.5)

    def __init__(self, launcher: Launcher):
        super().__init__()
        self.launcher = launcher
        self.timer = wpilib.Timer()
        self.addRequirements(self.launcher)

    def initialize(self) -> None:
        self.timer.reset()
        self.timer.start()

    def execute(self) -> None:
        self.launcher.extend_strong()

    def isFinished(self) -> bool:
        return self.timer.get() >= self.duration

    def end(self, interrupted: bool) -> None:
        self.launcher.stop()
