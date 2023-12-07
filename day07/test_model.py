from unittest import TestCase

from day07.model import Card, Hand


class TestCard(TestCase):

    def test_card_compare(self):
        c1 = Card('Q')
        c2 = Card('T')
        self.assertTrue(c1.value > c2.value)


five_of_a_kind = Hand([Card('A'), Card('A'), Card('A'), Card('A'), Card('A')])
four_of_a_kind = Hand([Card('A'), Card('A'), Card('A'), Card('A'), Card('6')])
full_house = Hand([Card('A'), Card('A'), Card('A'), Card('Q'), Card('Q')])
three_of_a_kind = Hand([Card('A'), Card('A'), Card('A'), Card('9'), Card('2')])
two_pairs = Hand([Card('A'), Card('A'), Card('K'), Card('K'), Card('5')])
one_pair = Hand([Card('A'), Card('A'), Card('9'), Card('2'), Card('3')])
high_card = Hand([Card('9'), Card('6'), Card('3'), Card('4'), Card('A')])


class TestHand(TestCase):

    def test_hand_ordering(self):
        self.assertTrue(five_of_a_kind > four_of_a_kind)
        self.assertTrue(four_of_a_kind > full_house)
        self.assertTrue(full_house > three_of_a_kind)
        self.assertTrue(three_of_a_kind > two_pairs)
        self.assertTrue(two_pairs > one_pair)
        self.assertTrue(one_pair > high_card)

    def test_hand_ordering_tie(self):
        h1 = Hand([Card('K'), Card('K'), Card('6'), Card('7'), Card('7')])
        h2 = Hand([Card('K'), Card('T'), Card('J'), Card('J'), Card('T')])
        self.assertTrue(h1 > h2)

    def test_hand_ordering_v2(self):
        h1 = Hand([Card('Q'), Card('Q'), Card('Q'), Card('J'), Card('A')], jokers=True)
        h2 = Hand([Card('Q'), Card('Q'), Card('Q'), Card('A'), Card('J')], jokers=True)
        self.assertTrue(h1 < h2)
