from collections import Counter
from dataclasses import dataclass

valid_cards = '23456789TJQKA'


class Card:
    label: str
    value: int = None

    def __init__(self, label):
        self.label = label
        self.value = valid_cards.index(label)

    def __repr__(self):
        return f"Card({self.label})"


class Hand(list[Card]):
    value: int

    def __init__(self, cards: list[Card], jokers=False):
        super().__init__(cards)
        if jokers:
            self.value = calc_value_v2(self)
        else:
            self.value = calc_value(self)

    def __lt__(self, other):
        if self.value == other.value:
            for i, card in enumerate(self):
                if card.value == other[i].value:
                    continue
                return card.value < other[i].value
            return True

        return self.value < other.value

    def __gt__(self, other):
        return not self < other


def calc_value(hand: Hand):
    counter = Counter(map(lambda c: c.label, hand))
    return sum(map(lambda c: c * c, counter.values()))


def calc_value_v2(hand: Hand):
    cards = []
    jokers = 0
    for card in hand:
        if card.label == 'J':
            jokers += 1
        else:
            cards.append(card)
    if jokers == 5:
        return jokers * jokers
    counter = Counter(map(lambda c: c.label, cards))
    mc = counter.most_common(1)[0]
    counter[mc[0]] += jokers
    return sum(map(lambda c: c * c, counter.values()))


@dataclass
class Bid:
    hand: Hand
    amount: int
