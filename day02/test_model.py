import unittest
from model import *


class TestModel(unittest.TestCase):

    def test_gamevalid_1(self):
        g = Game(1, [
            Set(1, 1, 1),
            Set(5, 1, 2)
        ])
        self.assertFalse(g.valid(3, 3, 3))

    def test_gamevalid_2(self):
        g = Game(2, [
            Set(4, 3, 2),
            Set(2, 2, 2)
        ])
        self.assertTrue(g.valid(5, 3, 3))
