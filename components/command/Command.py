class Command:
    def __init__(self, steering: float, vSpeed: float) -> None:
        self.steering = steering
        self.vSpeed = vSpeed

    def __eq__(self, other) -> bool:
        return self.steering == other.steering \
            and self.vSpeed == other.vSpeed

    def __repr__(self) -> str:
        return '(' + str(self.steering) \
            + ', ' + str(self.vSpeed) \
            + ')'

    def __str__(self) -> str:
        return '(steering: ' + str(self.steering) \
            + ', v_speed: ' + str(self.vSpeed) \
            + ')'
