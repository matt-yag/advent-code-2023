from math import sqrt, ceil, floor

FILE_PATH = 'input.txt'
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()

time = int(lines[0].split(':')[1].replace(' ', '').strip())
distance = int(lines[1].split(':')[1].replace(' ', '').strip())

delta = time ** 2 - 4 * distance
x1 = (time - sqrt(delta)) / 2
x2 = (time + sqrt(delta)) / 2
print(ceil(x2) - floor(x1) - 1)
