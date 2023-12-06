from functools import reduce
from math import sqrt, ceil, floor

FILE_PATH = 'input.txt'
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()

times = [int(lines[0].split(':')[1].replace(' ', ''))]
distances = [int(lines[1].split(':')[1].replace(' ', ''))]

results = []
for (index, time) in enumerate(times):
    delta = time ** 2 - 4 * distances[index]
    x1 = (time - sqrt(delta)) / 2
    x2 = (time + sqrt(delta)) / 2
    results.append(ceil(x2) - floor(x1) - 1)

print(reduce(lambda x, y: x * y, results))
