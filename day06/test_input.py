from unittest import TestCase

from day06.input import parse_input
from day06.model import Race


class TestInput(TestCase):
    def test_parse_input(self):
        races = parse_input('./input/test1.txt')
        expected = [Race(7, 9), Race(15, 40), Race(30, 200)]
        self.assertEqual(expected, races)
