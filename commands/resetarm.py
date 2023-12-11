from utils.property import autoproperty
from utils.safecommand import SafeCommand
from subsystems.arm import Arm


class ResetArm(SafeCommand):
    def __init__(self, arm: Arm):
        super().__init__()
        self.arm = arm
        self.addRequirements(self.arm)

    def execute(self):
        self.arm.moveUp()

    def isFinished(self) -> bool:
        return self.arm.is_at_limit_switch()

    def end(self, interrupted: bool):
        self.arm.resetEncoderPosition()
        self.arm.stop()
