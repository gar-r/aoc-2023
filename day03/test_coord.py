import unittest

from day03.coord import neighbors

test_data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


class TestCoord(unittest.TestCase):

    def test_neighbors_1(self):
        n = neighbors(test_data, (0, 0))
        expected = [2, 4, 5]
        self.assertEqual(expected, n)

    def test_neighbors_2(self):
        n = neighbors(test_data, (1, 1))
        expected = [1, 2, 3, 4, 6, 7, 8, 9]
        self.assertEqual(expected, n)

    def test_neighbors_3(self):
        n = neighbors(test_data, (2, 2))
        expected = [5, 6, 8]
        self.assertEqual(expected, n)
