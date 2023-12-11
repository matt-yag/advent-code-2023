import re

from utils import x, c, aoc


NEXT = {
    '|': lambda start, previous: (start[0] - 1, start[1]) if previous == (start[0] + 1, start[1]) else (start[0] + 1, start[1]),
    '-': lambda start, previous: (start[0], start[1] - 1) if previous == (start[0], start[1] + 1) else (start[0], start[1] + 1),
    'L': lambda start, previous: (start[0] - 1, start[1]) if previous == (start[0], start[1] + 1) else (start[0], start[1] + 1),
    'J': lambda start, previous: (start[0], start[1] - 1) if previous == (start[0] - 1, start[1]) else (start[0] -1, start[1]),
    '7': lambda start, previous: (start[0], start[1] -1) if previous == (start[0] + 1, start[1]) else (start[0] + 1, start[1]),
    'F': lambda start, previous: (start[0] + 1, start[1]) if previous == (start[0], start[1] + 1) else (start[0], start[1] + 1),
}

lines = aoc()

start = None
for index, line in enumerate(lines):
    if line.find('S') > -1:
        start = (index, line.find('S'))

def find_next(position):
    if position[0] > 0 and lines[position[0] - 1][position[1]] in ('|', 'F', '7'):
        return (position[0] - 1, position[1])
    if position[1] > 0 and lines[position[0]][position[1] - 1] in ('F', '-', 'L'):
        return (position[0], position[1] - 1)
    if position[0] + 1 < len(lines) and lines[position[0] + 1][position[1]] in ('|', 'L', 'J'):
        return (position[0] + 1, position[1])
    if position[1] + 1 < len(lines[0]) and lines[position[0]][position[1] +1 ] in ('-', 'J', '7'):
        return (position[0], position[1] + 1)


prev = start
current = find_next(start)
index = 0
c('--------')
c(prev)
c(current)
while current != start:
    next = NEXT[lines[current[0]][current[1]]](current, prev)
    c(next)
    prev = current
    current = next
    index += 1

c((index + 1) / 2)