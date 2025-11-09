class StrategyInterface:
    def generateSteering(self, steering: float) -> float:
        pass

    def generatePoints(self) -> int:
        pass
