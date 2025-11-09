import unittest
from components.coordinate.Coordinate import Coordinate
from components.part.Part import Part
from components.part.PartTransformer import PartTransformer


class PartTransformerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.partTransformer = PartTransformer()

    def testPresentForInput(self) -> None:
        with self.assertRaises(ValueError) as context:
            self.partTransformer.presentForInput(Part(
                coordinates=[],
                yaw=0.78,
                wSpeed=17.3,
            ))

        self.assertTrue('Must provide 2 coordinates' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.partTransformer.presentForInput(Part(
                coordinates=[Coordinate(x=1.2, y=3.4)],
                yaw=0.78,
                wSpeed=17.3,
            ))

        self.assertTrue('Must provide 2 coordinates' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.partTransformer.presentForInput(Part(
                coordinates=[
                    Coordinate(x=1.2, y=3.4),
                    Coordinate(x=5.6, y=7.8),
                ],
                yaw=0.78,
                wSpeed=17.3,
            ))

        self.assertTrue('First y coordinate must be 0' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.partTransformer.presentForInput(Part(
                coordinates=[
                    Coordinate(x=1.2, y=0.0),
                    Coordinate(x=5.6, y=7.8),
                    Coordinate(x=9.10, y=11.12),
                ],
                yaw=0.22,
                wSpeed=9.2,
            ))

        self.assertTrue('Must provide 2 coordinates' in str(context.exception))

        actual: list[float] = self.partTransformer.presentForInput(Part(
            coordinates=[
                Coordinate(x=1.2, y=0.0),
                Coordinate(x=5.6, y=7.8),
            ],
            yaw=0.15,
            wSpeed=3.9,
        ))
        self.assertEqual([1.2, 8.9554452709, 1.0571903221, 0.15, 3.9], actual)

    def testNormalizeToZero(self) -> None:
        with self.assertRaises(ValueError):
            self.partTransformer.normalizeToZero(Part(
                coordinates=[],
                yaw=1.49,
                wSpeed=91.7,
            ))

        with self.assertRaises(ValueError):
            self.partTransformer.normalizeToZero(Part(
                coordinates=[Coordinate(x=1.2, y=3.4)],
                yaw=1.49,
                wSpeed=91.7,
            ))

        actual: Part = self.partTransformer.normalizeToZero(Part(
            coordinates=[
                Coordinate(x=1.2, y=3.4),
                Coordinate(x=5.6, y=10.8),
                Coordinate(x=9.10, y=15.12),
            ],
            yaw=1.68,
            wSpeed=98.7,
        ))
        self.assertEqual(Part(
            coordinates=[
                Coordinate(x=8.6092973, y=0.0),
                Coordinate(x=14.1112562113, y=-0.8005299108)
            ],
            yaw=0.6456391308,
            wSpeed=98.7,
        ), actual)

        actual: Part = self.partTransformer.normalizeToZero(Part(
            coordinates=[
                Coordinate(x=1.2, y=3.4),
                Coordinate(x=5.6, y=10.8),
                Coordinate(x=9.10, y=15.12),
            ],
            yaw=-3.11,
            wSpeed=-58.2,
        ))
        self.assertEqual(Part(
            coordinates=[
                Coordinate(x=8.6092973, y=0.0),
                Coordinate(x=14.1112562113, y=-0.8005299108)
            ],
            yaw=2.138824438,
            wSpeed=-58.2,
        ), actual)
