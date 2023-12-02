from input import *
from model import *

games = parse('input/input.txt')

# part 1
sum = 0
for game in games:
    if game.valid(12, 13, 14):
        sum += game.number

print(sum)

# part 2
pow = 0
for game in games:
    mw = game.min_valid()
    pow += mw.pow()

print(pow)