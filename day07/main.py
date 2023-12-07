from day07 import model
from day07.input import parse_input


def main():
    filename = './input/input.txt'

    # part 1
    bids = parse_input(filename)
    bids.sort(key=lambda b: b.hand)
    print_winnings(bids)

    # part 2
    model.valid_cards = 'J23456789TQKA'     # change card values
    bids2 = parse_input(filename, jokers=True)
    bids2.sort(key=lambda b: b.hand)
    print_winnings(bids2)


def print_winnings(bids):
    winnings = 0
    for i, bid in enumerate(bids):
        winnings += (i + 1) * bid.amount
    print(winnings)


if __name__ == '__main__':
    main()
