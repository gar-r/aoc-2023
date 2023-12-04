import unittest

from day04.model import Card, parse_card


class TestCard(unittest.TestCase):
    def test_score_when_no_match(self):
        c = Card()
        c.winning_numbers = {1, 2, 3, 4}
        c.actual_numbers = {5, 6, 7, 8}
        self.assertEqual(0, c.score())

    def test_score_when_one_match(self):
        c = Card()
        c.winning_numbers = {1, 2, 3, 4}
        c.actual_numbers = {3, 6, 7, 8}
        self.assertEqual(1, c.score())

    def test_score_when_two_matches(self):
        c = Card()
        c.winning_numbers = {1, 2, 3, 4}
        c.actual_numbers = {1, 4, 7, 8}
        self.assertEqual(2, c.score())

    def test_score_when_three_matches(self):
        c = Card()
        c.winning_numbers = {1, 2, 3, 4}
        c.actual_numbers = {1, 2, 4, 8}
        self.assertEqual(4, c.score())


class TestParseCard(unittest.TestCase):

    def test_parse_1(self):
        c = parse_card('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53')
        self.assertEqual(1, c.identifier)
        self.assertEqual({41, 48, 83, 86, 17}, c.winning_numbers)
        self.assertEqual({83, 86, 6, 31, 17, 9, 48, 53}, c.actual_numbers)

    def test_parse_2(self):
        c = parse_card('Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36')
        self.assertEqual(5, c.identifier)
        self.assertEqual({87, 83, 26, 28, 32}, c.winning_numbers)
        self.assertEqual({88, 30, 70, 12, 93, 22, 82, 36}, c.actual_numbers)


if __name__ == '__main__':
    unittest.main()
