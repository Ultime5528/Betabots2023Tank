import math

from subsystems.drivetrain import Drivetrain
from utils.safecommand import CommandException


class AvancerX(CommandException):
    def __init__(self, drivetrain: Drivetrain, distanceX, distanceY, vitesseX, vitesseY):
        self.setName("AvancerX")
        super().__init__()

        self.drivetrain = drivetrain
        self.distanceX = distanceX
        self.distanceY = distanceY
        self.vitesseX = vitesseX
        self.vitesseY = vitesseY
        self.erreurX = math.inf
        self.erreurY = math.inf
        self.erreur_max = 0.1

        self.addRequirements(drivetrain)

    def initialize(self):
        self.drivetrain.resetOdometry()
        self.erreurX = math.inf
        self.erreurY = math.inf
        print(self.drivetrain.odometry.getPose().X(), self.drivetrain.odometry.getPose().Y())

    def execute(self):
        self.erreurX = self.distanceX - self.drivetrain.odometry.getPose().X()
        self.erreurY = self.distanceY - self.drivetrain.odometry.getPose().Y()

        self.vx = math.copysign(self.vitesseX, self.erreurX)
        self.vy = -math.copysign(self.vitesseY, self.erreurY)

        if abs(self.erreurX) <= self.erreur_max:
            self.vx = 0
        if abs(self.erreurY) <= self.erreur_max:
            self.vy = 0

        self.drivetrain.driveCartesian(self.vy, self.vx, 0)

    def end(self, interrupted: bool):
        self.drivetrain.driveCartesian(0, 0, 0)

    def isFinished(self) -> bool:
        return self.vx == 0 and self.vy == 0