import re

from utils import c, aoc

lines = aoc('-1')

instruction = lines[0]

map = {}
for line in lines[1:]:
    if line:
        map_line = re.findall(r'([0-9A-Z]+)\s*=\s*\(([^,]+),\s*([^,]+)\)', line)[0]
        map[map_line[0]] = (map_line[1], map_line[2])

start = 'AAA'
count = 0
while start != 'ZZZ':
    if instruction[count % len(instruction)] == 'L':
        start = map[start][0]
    elif instruction[count % len(instruction)] == 'R':
        start = map[start][1]
    else:
        raise Exception("Wrong instruction")
    count += 1

c(start, count)
