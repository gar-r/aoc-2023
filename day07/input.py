from day07.model import Bid, Hand, Card


def parse_input(filename, jokers=False):
    with open(filename) as f:
        bids = []
        for line in f:
            bids.append(parse_bid(line, jokers))
        return bids


def parse_bid(line: str, jokers: bool):
    parts = line.split(' ', maxsplit=2)
    return Bid(parse_hand(parts[0], jokers), int(parts[1]))


def parse_hand(s: str, jokers: bool):
    return Hand(list(map(lambda c: Card(c), s)), jokers)
