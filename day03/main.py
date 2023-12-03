from day03.coord import neighbors
from day03.input import parse_input, symbols


def get_part_numbers(d, coord):
    unique_part_numbers = {}
    ns = neighbors(d, coord)
    for n in ns:
        if isinstance(n, tuple):
            unique_part_numbers[n[0]] = n[1]
    return list(unique_part_numbers.values())


data = parse_input('./input/input.txt')

# part 1
part_numbers = []
for x, row in enumerate(data):
    for y, cell in enumerate(row):
        if isinstance(cell, str) and cell in symbols and cell != '.':
            part_numbers.extend(get_part_numbers(data, (x, y)))

print(sum(part_numbers))

# part 2
gears_sum = 0
for x, row in enumerate(data):
    for y, cell in enumerate(row):
        if cell == '*':
            part_numbers = get_part_numbers(data, (x, y))
            if len(part_numbers) == 2:
                gears_sum += (part_numbers[0] * part_numbers[1])

print(gears_sum)
