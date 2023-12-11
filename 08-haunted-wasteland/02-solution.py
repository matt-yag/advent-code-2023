import re
from utils import c, aoc

lines = aoc()


def gcd(x, y):
    while y != 0:
        tmp = y
        y = a % y
        a = tmp
    return a


instruction = lines[0]

map = {}
for line in lines[1:]:
    if line:
        map_line = re.findall(r'([0-9A-Z]+)\s*=\s*\(([^,]+),\s*([^,]+)\)', line)[0]
        map[map_line[0]] = (map_line[1], map_line[2])

nodes = [node for node in map.keys() if node[-1] == 'A']
results = []
for start in nodes:
    count = 0
    while start[-1] != 'Z':
        if instruction[count % len(instruction)] == 'L':
            start = map[start][0]
        elif instruction[count % len(instruction)] == 'R':
            start = map[start][1]
        else:
            raise Exception("Wrong instruction")
        count += 1
    results.append(count)

while len(results) > 1:
    a = results.pop(0)
    b = results.pop(0)
    results.append(a * b / gcd(a, b))

c(int(results[0]))
