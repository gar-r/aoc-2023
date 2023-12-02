import unittest

from input import *
from model import *


class TestInput(unittest.TestCase):

    def test_parseline(self):
        tests = [
            {
                'line': 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
                'expected': Game(1, [
                    Set(4, 0, 3),
                    Set(1, 2, 6),
                    Set(0, 2, 0)
                ])
            },
            {
                'line': 'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
                'expected': Game(2, [
                    Set(0, 2, 1),
                    Set(1, 3, 4),
                    Set(0, 1, 1)
                ])
            },
            {
                'line': 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
                'expected': Game(3, [
                    Set(20, 8, 6),
                    Set(4, 13, 5),
                    Set(1, 5, 0)
                ])
            },
            {
                'line': 'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
                'expected': Game(4, [
                    Set(3, 1, 6),
                    Set(6, 3, 0),
                    Set(14, 3, 15)
                ])
            },
            {
                'line': 'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
                'expected': Game(5, [
                    Set(6, 3, 1),
                    Set(1, 2, 2)
                ])
            },
        ]

        for test in tests:
            self.assertEqual(test['expected'], parseline(test['line']))


if __name__ == '__main__':
    unittest.main()
