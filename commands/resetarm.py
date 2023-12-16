import commands2
from commands.movearm import MoveArm
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
            commands2.WaitCommand(0.5)
            self.arm.resetEncoderPosition()


class ResetProtocol(commands2.SequentialCommandGroup):
    def __init__(self, arm: Arm):
        super().__init__(
            MoveArm.toLevel2(arm),
            ResetArm(arm),
            MoveArm.toLevel3(arm)
        )

