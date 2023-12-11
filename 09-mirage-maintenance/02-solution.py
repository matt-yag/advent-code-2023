import re

from utils import x, c, aoc

lines = aoc()


def diff(numbers):
    c(numbers)
    new_numbers = []
    for (index, number) in enumerate(numbers[:-1]):
        new_numbers.append(numbers[index + 1] - number)
    if len([x for x in new_numbers if x == 0]) == len(new_numbers):
        return 0
    else:
        numbers_ = new_numbers[0] - diff(new_numbers)
        c(numbers_)
        return numbers_


r = []
for line in lines:
    numbers = [int(number) for number in line.split(' ')]
    r.append(int(numbers[0]) - diff(numbers))
    print(r[-1])
print(r)
c(x(r))
