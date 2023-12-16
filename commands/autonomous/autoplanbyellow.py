import commands2
from commands2._impl.cmd import parallel

from commands.launch import Launch
from subsystems.arm import Arm
from commands.resetarm import ResetArm
from subsystems.launcher import Launcher
from commands.autonomous.avancerx import AvancerX
from subsystems.drivetrain import Drivetrain


import commands2
from commands2._impl.cmd import parallel

from commands.autonomous.tournerx import TournerX
from commands.launch import Launch
from subsystems.arm import Arm
from commands.resetarm import ResetArm
from subsystems.launcher import Launcher
from commands.autonomous.avancerx import AvancerX
from subsystems.drivetrain import Drivetrain


class AutoPlanBGreen(commands2.SequentialCommandGroup):
    def __init__(self, drivetrain: Drivetrain, launcher: Launcher, arm: Arm):
        super().__init__(
            parallel(
                commands2.SequentialCommandGroup(
                    AvancerX(drivetrain, 1, 1),
                    TournerX(drivetrain, -45, 1),
                    AvancerX(drivetrain, 1, 1)
                ),
                ResetArm(arm)
            ),
            Launch(launcher),
            AvancerX(drivetrain, -1, 1),
            TournerX(drivetrain, -90, 1),
            AvancerX(drivetrain, 1, 1)
        )
