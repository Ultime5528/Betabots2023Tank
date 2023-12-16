import commands2

from commands.autonomous.autonomousfirststeps import AutonomousFirstSteps
#from commands.tournerX import TournerX
from avancerx import AvancerX
from commands.autonomous.tournerx import TournerX
from subsystems.arm import Arm
from subsystems.launcher import Launcher

from subsystems.drivetrain import Drivetrain

#values for AvancerX are to be changed
class AutonomousYellow(commands2.SequentialCommandGroup):
    def __init__(self, arm: Arm, drivetrain: Drivetrain, launcher: Launcher):
        super().__init__(
            AutonomousFirstSteps(arm, drivetrain, launcher),
            TournerX(drivetrain, 90, 1),
            AvancerX(drivetrain, 1, 1)
        )
