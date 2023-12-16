import commands2

from subsystems.launcher import Launcher
from subsystems.drivetrain import Drivetrain
from commands.autonomous.urgence import BougerUrgence
from commands.launch import Launch

class AutoUrgence(commands2.SequentialCommandGroup):
    def __init__(self, drivetrain: Drivetrain, launcher: Launcher):
        super().__init__(
            BougerUrgence(drivetrain, 0.5, 2, 0),
            BougerUrgence(drivetrain, 0, 0.5, 0.3),
            Launch(launcher),
            Launch(launcher)
        )
