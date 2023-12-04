import math


class Card:
    identifier: int
    winning_numbers: set[int]
    actual_numbers: set[int]

    def score(self):
        matches = self.matches()
        if matches == 0:
            return 0
        return pow(2, matches - 1)

    def matches(self):
        return len(self.actual_numbers.intersection(self.winning_numbers))

    def __repr__(self) -> str:
        return f"Card({self.identifier=})"


def parse_card(s: str):
    parts = s.split(':')
    c = Card()
    c.identifier = parse_identifier(parts[0])
    (c.winning_numbers, c.actual_numbers) = parse_numbers(parts[1])
    return c


def parse_identifier(s: str):
    return int(s.replace('Card ', ''))


def parse_numbers(s: str):
    parts = s.split('|')
    return parse_list(parts[0]), parse_list(parts[1])


def parse_list(s: str):
    parts = s.strip().split(' ')
    res = set()
    for part in parts:
        if part == '':
            continue
        res.add(int(part))
    return res
