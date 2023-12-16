import commands2
from commands2._impl.cmd import parallel

from commands.launch import Launch
from subsystems.arm import Arm
from commands.resetarm import ResetArm
from subsystems.launcher import Launcher
from commands.autonomous.avancerx import AvancerX
from subsystems.drivetrain import Drivetrain

# values in AvancerX are to be changed #
class AutonomousFirstSteps(commands2.SequentialCommandGroup):
    def __init__(self, arm: Arm, launcher: Launcher, drivetrain: Drivetrain):
        super().__init__(
            parallel(
                AvancerX(drivetrain, 1, 1),
                ResetArm(arm)
            ),
            Launch(launcher),
            AvancerX(drivetrain, -1, 1)
        )
