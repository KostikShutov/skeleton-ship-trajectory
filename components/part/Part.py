from components.coordinate.Coordinate import Coordinate


class Part:
    def __init__(self, coordinates: list[Coordinate], yaw: float, wSpeed: float) -> None:
        self.coordinates = coordinates
        self.yaw = round(yaw, 10)
        self.wSpeed = round(wSpeed, 10)

    def __eq__(self, other) -> bool:
        return self.coordinates == other.coordinates \
            and self.yaw == other.yaw \
            and self.wSpeed == other.wSpeed

    def __repr__(self) -> str:
        return '(' + str(self.coordinates) \
            + ', ' + str(self.yaw) \
            + ', ' + str(self.wSpeed) \
            + ')'

    def __str__(self) -> str:
        return '(coordinates: ' + str(self.coordinates) \
            + ', yaw: ' + str(self.yaw) \
            + ', w_speed: ' + str(self.wSpeed) \
            + ')'
