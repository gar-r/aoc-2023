from model import *


def parse(name: str):
    res = []
    with open(name) as f:
        for line in f:
            res.append(parseline(line))

    return res


def parseline(line: str):
    parts = line.split(sep=':', maxsplit=2)
    return Game(
        number=parse_number(parts[0]),
        sets=parse_sets(parts[1]))


def parse_number(s: str):
    return int(s.replace('Game ', ''))


def parse_sets(s: str):
    res = []
    parts = s.split(';')
    for part in parts:
        res.append(parse_set(part.strip()))
    return res


def parse_set(s: str):
    res = Set(0, 0, 0)
    parts = s.split(',', maxsplit=3)
    for part in parts:
        if 'red' in part:
            res.R = parse_count(part)
        if 'blue' in part:
            res.B = parse_count(part)
        if 'green' in part:
            res.G = parse_count(part)
    return res


def parse_count(s: str):
    return int(s.strip().split(' ')[0])
