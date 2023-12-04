import unittest

from day04.main import calc_total_score
from day04.model import Card


def get_test_card(winning_numbers, actual_numbers):
    c = Card()
    c.winning_numbers = winning_numbers
    c.actual_numbers = actual_numbers
    return c


class TestTotalScore(unittest.TestCase):
    def test_calc_total_score(self):
        cards = [
            get_test_card({1, 2, 3}, {3, 4, 5}),    # score = 1
            get_test_card({1, 2, 3}, {1, 2, 3}),    # score = 4
            get_test_card({1, 2, 3}, {1, 2, 5}),    # score = 2
        ]
        self.assertEqual(7, calc_total_score(cards))


if __name__ == '__main__':
    unittest.main()
