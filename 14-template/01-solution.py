import re

from utils import a, o, c, aoc

lines = aoc()
lines_count = len(lines)

blockers = [lines_count + 1] * len(lines[0])
counters = [0] * len(lines[0])
sum = 0
for (index, line) in enumerate(lines):
    for (i, c) in enumerate(line):
        if c == 'O':
            counters[i] += 1
        elif c == '#':
            if counters[i]:
                sum += (blockers[i] * (blockers[i] - 1) - (blockers[i] - counters[i]) * (blockers[i] - 1 - counters[i])) / 2
                counters[i] = 0
            blockers[i] = lines_count - index

for (i, counter) in enumerate(counters):
    if counter:
        sum += (blockers[i] * (blockers[i] - 1) - (blockers[i] - counters[i]) * (blockers[i] - 1 - counters[i])) / 2

print(sum)


