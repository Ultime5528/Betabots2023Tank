import commands2

from commands.autonomousfirststeps import AutonomousFirstSteps
#from commands.tournerX import TournerX
from avancerx import AvancerX
from subsystems.arm import Arm
from commands.resetarm import ResetArm
from subsystems.launcher import Launcher

from subsystems.drivetrain import Drivetrain

#values for AvancerX are to be changed
class AutonomousYellow(commands2.SequentialCommandGroup):
    def __init__(self, arm: Arm, drivetrain: Drivetrain, launcher: Launcher):
        super().__init__(
            AutonomousFirstSteps(arm, drivetrain, launcher),
            #tournerX(drivetrain)
            AvancerX(drivetrain, 1, 1)
        )