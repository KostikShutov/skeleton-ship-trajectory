import math
import random
from components.config.TrainConfig import TrainConfig
from components.model.StrategyInterface import StrategyInterface


class ShipStrategy(StrategyInterface):
    def generateSteering(self, steering: float) -> float:  # [rad]
        delta: float = math.radians(float(random.randint(-5, 5)))  # [rad]

        return max(TrainConfig.MIN_STEERING, min(TrainConfig.MAX_STEERING, steering + delta))  # [rad]

    def generatePoints(self) -> int:
        return random.randint(1, 10)
