from day05.mapper import Range, MapperChain, MapperList, Mapper
from day05.range import RangeList


def read_lines(filename):
    with open(filename, 'r') as f:
        return f.readlines()


def parse_input(lines: list[str], seed_fn=None):
    if seed_fn is None:
        seed_fn = parse_seeds_v1
    seeds = seed_fn(lines[0])
    mapper_chain = parse_mapper_chain(lines[2:])
    return seeds, mapper_chain


def parse_seeds_v1(s: str):
    res = RangeList()
    parts = s.replace('seeds: ', '').split(' ')
    for part in parts:
        res.append(Range(int(part), 1))
    return res


def parse_seeds_v2(s: str):
    res = RangeList()
    parts = s.replace('seeds: ', '').split(' ')
    for i in range(0, len(parts), 2):
        start = parts[i]
        size = parts[i+1]
        res.append(Range(int(start), int(size)))
    return res


def parse_mapper_chain(lines: list[str]):
    res = MapperChain()
    start = 0
    for i, line in enumerate(lines):
        if is_empty(line):
            res.append(parse_mapper_list(lines[start:i]))
            start = i + 1
    res.append(parse_mapper_list(lines[start:]))
    return res


def parse_mapper_list(lines: list[str]):
    res = MapperList()
    for line in lines:
        if 'map' in line:
            continue  # skip header
        res.append(parse_mapper(line))
    return res


def parse_mapper(line: str):
    parts = line.split(' ', maxsplit=3)
    return Mapper(int(parts[1]), int(parts[2]), int(parts[0]))


def is_empty(line):
    return len(line.strip()) == 0
