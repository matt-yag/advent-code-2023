import sys
from functools import reduce


def a(list):
    """Returns a sum of all elements in the list"""
    return reduce(lambda x, y: x + y, list)


def o(list):
    """Returns a product of all elements in the list"""
    return reduce(lambda x, y: x * y, list)


def c(*args):
    """Prints element"""
    print(args)


def aoc(sufix=''):
    if len(sys.argv) == 1:
        file_path = 'input.txt'
    else:
        file_path = 'input-test%s.txt' % sufix
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines
