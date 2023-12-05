import sys
from itertools import repeat
from multiprocessing.pool import Pool

from day05.input import parse_input, read_lines, parse_seeds_v1, parse_seeds_v2


def main():

    data = read_lines('./input/input.txt')
    # part 1
    print(min_seed(data, parse_seeds_v1))
    # part 2
    print(min_seed(data, parse_seeds_v2))


def min_seed(filename, seed_fn):
    (seeds, mappers) = parse_input(filename, seed_fn)
    with Pool() as pool:
        return min(pool.starmap(calc_seed_range, zip(seeds, repeat(mappers))))


def calc_seed_range(seed, mappers):
    return min(map(mappers.remap, range(seed.start, seed.start + seed.length)))


if __name__ == "__main__":
    main()
