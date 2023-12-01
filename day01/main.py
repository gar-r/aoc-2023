pseudodigits = {
    'one': 'o1e',
    'two': 't2o',
    'three': 'thr3e',
    'four': 'fo4r',
    'five': 'f5ve',
    'six': 's6x',
    'seven': 'se7en',
    'eight': 'ei8ht',
    'nine': 'ni9e'
}

def fixdigits(str):
    for k in pseudodigits:
        str = str.replace(k, pseudodigits[k])
    return str


def first(line):
    for c in line:
        if c.isdigit():
            return int(c)
    return 0


def last(line):
    return first(line[::-1])


def value(line):
    fixedline = fixdigits(line)
    f = first(fixedline)
    l = last(fixedline)
    return 10 * f + l


with open('input.txt', 'r') as f:
    sum = 0
    for line in f:
        sum += value(line)
    print(sum)