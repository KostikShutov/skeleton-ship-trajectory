import os
import json
import math
import numpy as np
import matplotlib.pyplot as plt
from collections.abc import Iterable
from helpers.Utility import parseArgs
from components.config.TrainConfig import TrainConfig


def addSteerings(steerings: dict) -> None:
    plt.figure()
    plt.xticks(ticks=np.arange(int(round(math.degrees(TrainConfig.MIN_STEERING), 0)),
                               int(round(math.degrees(TrainConfig.MAX_STEERING), 0)) + 1,
                               1),
               rotation=90,
               fontsize=8)
    plt.bar(x=steerings.keys(), height=steerings.values())  # noqa
    plt.title('Распределение угла поворота пера руля')
    plt.xlabel('Значение [deg]')
    plt.ylabel('Количество')
    plt.savefig('distribution-picture-steerings.png', bbox_inches='tight', dpi=300)


def addSpeeds(speeds: dict) -> None:
    plt.figure()
    plt.xticks(ticks=[TrainConfig.V_SPEED])
    plt.bar(x=speeds.keys(), height=speeds.values())  # noqa
    plt.title('Распределение скорости движения')
    plt.xlabel('Значение [m/s]')
    plt.ylabel('Количество')
    plt.savefig('distribution-picture-speeds.png', bbox_inches='tight', dpi=300)


def distribute(path: str) -> None:
    with open(path, 'r') as file:
        items: Iterable = json.load(file)

    steerings: dict = {}
    speeds: dict = {}

    for item in items:
        steering: int = int(round(math.degrees(item['steering']), 0))
        steerings[steering] = steerings.get(steering, 0) + 1

        speed: float = float(round(item['v_speed'], 2))
        speeds[speed] = speeds.get(speed, 0) + 1

    addSteerings(steerings)
    addSpeeds(speeds)
    plt.show()


def main() -> None:
    args: any = parseArgs()
    modelFile: str = 'model/' + args.model + '/' + args.file + '.json'

    print('---Running ' + os.path.basename(__file__) + '---')
    print('Model file: ' + modelFile)

    distribute(path=modelFile)


if __name__ == '__main__':
    main()
