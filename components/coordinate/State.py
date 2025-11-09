class State:
    def __init__(self, yaw: float, steering: float, vSpeed: float, wSpeed: float) -> None:
        self.yaw = round(yaw, 10)
        self.steering = round(steering, 10)
        self.vSpeed = round(vSpeed, 10)
        self.wSpeed = round(wSpeed, 10)

    def __eq__(self, other) -> bool:
        return self.yaw == other.yaw \
            and self.steering == other.steering \
            and self.vSpeed == other.vSpeed \
            and self.wSpeed == other.wSpeed

    def __repr__(self) -> str:
        return '(' + str(self.yaw) \
            + ', ' + str(self.steering) \
            + ', ' + str(self.vSpeed) \
            + ', ' + str(self.wSpeed) \
            + ')'

    def __str__(self) -> str:
        return '(yaw: ' + str(self.yaw) \
            + ', steering: ' + str(self.steering) \
            + ', v_speed: ' + str(self.vSpeed) \
            + ', w_speed: ' + str(self.wSpeed) \
            + ')'
