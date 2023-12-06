
import math

from subsystems.drivetrain import Drivetrain
from utils.safecommand import SafeCommand


class AvancerX(SafeCommand):
    def __init__(self, base_pilotable: Drivetrain, distanceX, vitesseX):
        super().__init__()

        self.base_pilotable = base_pilotable
        self.distanceX = distanceX
        self.vitesseX = vitesseX
        self.erreurX = math.inf
        self.erreur_max = 0.1

        self.addRequirements(base_pilotable)

    def initialize(self):
        self.base_pilotable.resetOdometry()
        self.erreurX = math.inf


    def execute(self):
        self.erreurX = self.distanceX - self.base_pilotable.odometry.getPose().X()

        self.vx = math.copysign(self.vitesseX, self.erreurX)

        if abs(self.erreurX) <= self.erreur_max:
            self.vx = 0

    def isFinished(self) -> bool:
        return self.vx == 0