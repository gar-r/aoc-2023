from day06.model import Race


def parse_input(filename, extract_fn=None):
    if extract_fn is None:
        extract_fn = extract_data
    with open(filename) as f:
        return parse_races(f.readlines(), extract_fn)


def parse_races(lines, extract_fn):
    data = list(map(extract_fn, lines))
    res = []
    for i, _ in enumerate(data[0]):
        time = int(data[0][i])
        dtb = int(data[1][i])
        res.append(Race(time, dtb))
    return res


def extract_data(line: str):
    return line.replace('Time:', '').replace('Distance:', '').strip().split()


def extract_data_v2(line: str):
    return [line.replace('Time:', '').replace('Distance:', '').replace(' ', '')]
