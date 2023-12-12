from subsystems.arm import Arm
from utils.safecommand import SafeCommand


class ResetArm(SafeCommand):
    def __init__(self, arm: Arm):
        super().__init__()
        self.arm = arm
        self.addRequirements(self.arm)

    def execute(self):
        self.arm.moveUp()

    def isFinished(self) -> bool:
        return self.arm.is_up()

    def end(self, interrupted: bool):
        self.arm.stop()
        if not interrupted:
            self.arm.resetEncoderPosition()
