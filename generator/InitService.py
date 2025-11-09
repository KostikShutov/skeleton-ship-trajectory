import math
from components.config.InitConfig import InitConfig
from components.config.TrainConfig import TrainConfig
from components.coordinate.Coordinate import Coordinate
from components.coordinate.CoordinateTransformer import CoordinateTransformer


class InitService:
    def __init__(self, coordinateTransformer: CoordinateTransformer) -> None:
        self.coordinateTransformer = coordinateTransformer

    def init(self, course: list[Coordinate]) -> object:
        if not course:
            return []

        result: list[list[object]] = []
        course: list[Coordinate] = self.coordinateTransformer.addFictionalCoordinate(coordinates=course)
        fragments: list[list[Coordinate]] = self.coordinateTransformer.splitInfoFragments(coordinates=course)

        for fragment in fragments:
            result.append([{'x': c.x, 'y': c.y} for c in fragment])

        return {
            'config': {
                'yaw': math.radians(InitConfig.YAW),
                'w_speed' : InitConfig.W_SPEED,
                't_coefficient' : TrainConfig.T_COEFFICIENT,
                'c_coefficient' : TrainConfig.C_COEFFICIENT,
                'k_coefficient' : TrainConfig.K_COEFFICIENT,
            },
            'fragments': result,
        }
