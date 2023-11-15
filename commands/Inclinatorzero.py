import wpilib
from utils.safecommand import SafeCommand
from subsystems.inclinator import Inclinator

class MoveToZero(SafeCommand):
    def __init__(self, inclinator: Inclinator):
        super().__init__()
        self.inclinator = inclinator
        self.addRequirements(self.inclinator)

    def execute(self):
        self.inclinator.moveDown()

    def isFinished(self) -> bool:
        return self.inclinator.getLimitswitchValue()

    def end(self, interrupted: bool):
        self.inclinator.stop()
