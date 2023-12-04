from day04.model import parse_card, Card


def parse_cards(filename):
    res = []
    with open(filename) as f:
        for line in f:
            c = parse_card(line)
            res.append(c)
    return res


def calc_total_score(card_list):
    return sum(map(Card.score, card_list))


cards = parse_cards('./input/input.txt')

# part 1
print(calc_total_score(cards))

# part 2
stack = cards.copy()
stack.reverse()     # reverse to convert to stack
count = 0
while len(stack) > 0:
    c = stack.pop()
    count += 1
    m = c.matches()
    if m > 0:
        for i in range(m, 0, -1):
            stack.append(cards[c.identifier + i - 1])

print(count)
