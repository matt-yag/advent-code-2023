import re

from utils import a, o, c, aoc

lines = aoc()

columns = set([])
galaxies = []
resize_by = 0
for (y, line) in enumerate(lines):
    if '#' not in line:
        resize_by += (1000000 - 1)
    else:
        columns.update([m.start() for m in re.finditer('#', line)])
        galaxies += [(m.start(), y + resize_by) for m in re.finditer('#', line)]

total_distance = 0
for (i, galaxy_1) in enumerate(galaxies):
    for (j, galaxy_2) in enumerate(galaxies):
        if i < j:
            start = min(galaxy_1[0], galaxy_2[0])
            end = max(galaxy_1[0], galaxy_2[0])
            non_empty_columns = len([x for x in columns if start < x <= end])
            distance_x = abs(galaxy_2[0] - galaxy_1[0])
            distance_y = abs(galaxy_2[1] - galaxy_1[1])
            distance = distance_x + distance_y + (max(distance_x - non_empty_columns, 0) * (1000000 - 1))
            total_distance += distance

c(total_distance)
