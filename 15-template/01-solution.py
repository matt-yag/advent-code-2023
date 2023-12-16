import re

from utils import a, o, c, aoc

lines = aoc()


def h(text):
    hash = 0

    for c in text:
        hash += ord(c)
        hash *= 17
        hash %= 256
    return hash

values = lines[0].split(',')
c(a([h(v) for v in values]))