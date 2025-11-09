from components.model.ModelName import ModelName
from components.model.ShipStrategy import ShipStrategy
from components.model.StrategyInterface import StrategyInterface


class StrategyResolver:
    def resolve(self, modelName: ModelName) -> StrategyInterface:
        if modelName == ModelName.SHIP:
            return ShipStrategy()

        raise NotImplementedError('Model not implemented')
