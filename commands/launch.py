import commands2

from commands.extend import ExtendStrong
from subsystems.launcher import Launcher
from commands.retract import Retract


class Launch(commands2.SequentialCommandGroup):
    def __init__(self, launcher: Launcher):
        super().__init__(
            ExtendStrong(launcher),
            commands2.WaitCommand(0.1),
            Retract(launcher)
        )
