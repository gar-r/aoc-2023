import math
from functools import reduce
from operator import mul

from day06.input import parse_input, extract_data_v2
from day06.model import Race


def main():
    # part 1
    races = parse_input('./input/input.txt')
    print(reduce(mul, map(count_improvements, races), 1))

    # part 2
    races = parse_input('./input/input.txt', extract_fn=extract_data_v2)
    print(reduce(mul, map(count_improvements, races), 1))


def count_improvements(r: Race):
    target = find_target(r)
    optimum = math.floor(r.time / 2)
    count = (optimum - target) * 2
    if count > 0 and r.time % 2 == 0:
        count -= 1
    return count


def find_target(r: Race):
    lower = 0
    upper = r.time
    while True:
        charge = lower + round((upper - lower) / 2)
        if upper - lower <= 1:
            return charge
        d = r.calc_distance(charge)
        if d > r.dtb:
            upper = charge
        elif d < r.dtb:
            lower = charge
        else:
            return charge


if __name__ == '__main__':
    main()
