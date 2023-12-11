import re

from utils import a, o, c, aoc

lines = aoc()

columns = set([])
galaxies = []
add = 0
for (y, line) in enumerate(lines):
    if '#' not in line:
        add += (2 - 1)
    else:
        columns.update([m.start() for m in re.finditer('#', line)])
        galaxies += [(m.start(), y + add) for m in re.finditer('#', line)]

list_of_columns = list(columns)
list_of_columns.sort()
print(list_of_columns)
sum = 0
for (i, galaxy_1) in enumerate(galaxies):
    for (j, galaxy_2) in enumerate(galaxies):
        if i < j:
            start = min(galaxy_1[0], galaxy_2[0])
            end = max(galaxy_1[0], galaxy_2[0])
            plus = len([x for x in list_of_columns if start < x < end])
            distance_x = abs(galaxy_2[0] - galaxy_1[0])
            distance = distance_x + abs(galaxy_2[1] - galaxy_1[1]) + (max(distance_x - 1 - plus, 0) * (2 - 1))
            sum += distance
c(sum)
