import commands2

from commands.extendlauncher import Extend
from subsystems.launcher import Launcher
from commands.retractlauncher import Retract


class Launch(commands2.SequentialCommandGroup):
    def __init__(self, launcher: Launcher):
        super().__init__(
            Extend(launcher),
            commands2.WaitCommand(0.1),
            Retract(launcher)
        )

