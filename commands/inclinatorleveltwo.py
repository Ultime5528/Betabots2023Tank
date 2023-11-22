from utils.safecommand import SafeCommand
from subsystems.inclinator import Inclinator
from utils.property import autoproperty

#this command aims for the lower flowers
class MoveToLevelTwo(SafeCommand):
    two_encoder_value = autoproperty(20)
    interval = autoproperty(1)
    def __init__(self, inclinator: Inclinator):
        super().__init__()
        self.inclinator = inclinator
        self.addRequirements(self.inclinator)

    def execute(self):
        if (self.two_encoder_value < self.inclinator.getEncoderPosition()):
            self.inclinator.moveDown()
        elif (self.two_encoder_value > self.inclinator.getEncoderPosition()):
            self.inclinator.moveUp()
        else:
            self.inclinator.stop()

        self.inclinator.updateEncoderPosition()

    def isFinished(self) -> bool:
        return self.isBetweenValues(self.two_encoder_value - self.interval, self.two_encoder_value + self.interval,
                                    self.inclinator.getEncoderPosition())

    def end(self, interrupted: bool):
        self.inclinator.stop()

    def isBetweenValues(self, minInterval, maxInterval, value):
        return value >= minInterval and value <= maxInterval