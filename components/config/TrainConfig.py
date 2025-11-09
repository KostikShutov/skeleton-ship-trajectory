class TrainConfig:
    X: float = 0.0  # [m]
    Y: float = 0.0  # [m]
    YAW: float = 0.0  # [rad]
    STEERING: float = 0.0  # [rad]
    MIN_STEERING: float = -0.6108652381980153  # [rad]
    MAX_STEERING: float = 0.6108652381980153  # [rad]
    V_SPEED: float = 3  # [m/s]
    W_SPEED: float = 0.0  # [rad/s]
    T_COEFFICIENT: float = 6.0
    C_COEFFICIENT: float = 0.7
    K_COEFFICIENT: float = 1.5
    DURATION: float = 0.1  # [s]
