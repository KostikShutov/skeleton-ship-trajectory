import os
import math
import json
from tqdm import tqdm
from components.config.TrainConfig import TrainConfig
from components.model.ModelName import ModelName
from components.model.StrategyInterface import StrategyInterface
from components.model.StrategyResolver import StrategyResolver
from helpers.Utility import createDirectory, parseArgs
from helpers.Math import normalizeAngle


def generateTrajectory(strategy: StrategyInterface, number: int) -> list[object]:
    x: float = TrainConfig.X  # [m]
    y: float = TrainConfig.Y  # [m]
    yaw: float = TrainConfig.YAW  # [rad]
    steering: float = TrainConfig.STEERING  # [rad]
    vSpeed: float = TrainConfig.V_SPEED  # [m/s]
    wSpeed: float = TrainConfig.W_SPEED  # [rad/s]
    points: int = strategy.generatePoints()
    result: list[object] = [{
        'x': x,
        'y': y,
        'yaw': yaw,
        'steering': steering,
        'v_speed': vSpeed,
        'w_speed': wSpeed,
    }]

    for _ in tqdm(range(number), desc='Generating trajectory'):
        for _ in range(points):
            x += vSpeed * math.sin(yaw) * TrainConfig.DURATION  # [m]
            y += vSpeed * math.cos(yaw) * TrainConfig.DURATION  # [m]
            yaw += wSpeed * TrainConfig.DURATION  # [rad]
            yaw: float = normalizeAngle(yaw)  # [rad]
            wSpeed += (TrainConfig.K_COEFFICIENT * steering - wSpeed - TrainConfig.C_COEFFICIENT * wSpeed * abs(wSpeed)) / TrainConfig.T_COEFFICIENT * TrainConfig.DURATION  # [rad/s]

        steering: float = strategy.generateSteering(steering)  # [rad]
        points: int = strategy.generatePoints()

        result.append({
            'x': x,
            'y': y,
            'yaw': yaw,
            'steering': steering,
            'v_speed': vSpeed,
            'w_speed': wSpeed,
        })

    return result


def saveTrajectory(path: str, trajectory: list[object]) -> None:
    with open(path, 'w') as file:
        file.write(json.dumps(trajectory))
        file.write('\n')


def main() -> None:
    args: any = parseArgs()
    number: int = args.number
    modelName: str = args.model
    modelDirectory: str = 'model/' + modelName + '/'
    modelFile: str = modelDirectory + args.file + '.json'

    print('---Running ' + os.path.basename(__file__) + '---')
    print('Model file: ' + modelFile)
    print('Number: ' + str(number))

    strategy: StrategyInterface = StrategyResolver().resolve(modelName=ModelName(modelName))
    trajectory: list[object] = generateTrajectory(strategy=strategy, number=number)
    createDirectory(directory=modelDirectory)
    saveTrajectory(path=modelFile, trajectory=trajectory)


if __name__ == '__main__':
    main()
