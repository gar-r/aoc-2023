symbols = '~!@#$%^&*()-=_+{}[]|,./<>?'


def parse_input(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            if len(line.strip()) > 0:
                data.append(get_numbers(line))
    return data


def get_numbers(line: str):
    res = []
    current_number = ''
    for c in line:
        if c in symbols:
            if current_number != '':
                i = new_id()
                for _ in current_number:
                    res.append((i, int(current_number)))
                current_number = ''
            res.append(c)
        elif c.isdigit():
            current_number += c
    if current_number != '':
        i = new_id()
        for _ in current_number:
            res.append((i, int(current_number)))
    return res


identifier = 0


def new_id():
    global identifier
    res = identifier
    identifier += 1
    return res
