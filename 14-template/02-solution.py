import re

from utils import a, o, c, aoc

lines = aoc()


def b(lines):
    for line in lines:
        text = ''
        for c in line:
            text += c
        print(text)
    print('------------')


def new_text(text):
    counter_o = 0
    counter_dot = 0
    result = ''
    for c in text:
        if c == '.':
            counter_dot += 1
        elif c == 'O':
            counter_o += 1
        elif c == '#':
            result += ('O' * counter_o) + ('.' * counter_dot) + '#'
            counter_o = 0
            counter_dot = 0
    result += ('O' * counter_o) + ('.' * counter_dot)
    return result


b(lines)

saw = []
saw.append("\n".join(lines))
cycle = 0
result = None
while True:
    cycle += 1
    new_lines = [['' for x in range(len(lines[0]))] for y in range(len(lines))]
    for i in range(len(lines[0])):
        text = ''
        for j in range(len(lines)):
            text += lines[j][i]
        text = new_text(text)
        for j in range(len(text)):
            new_lines[j][i] = text[j]

    lines = new_lines
    new_lines = []

    for i in range(len(lines)):
        text = lines[i]
        text = new_text(text)
        new_lines.append(text)

    lines = new_lines
    new_lines = [['' for x in range(len(lines[0]))] for y in range(len(lines))]
    for i in range(len(lines[0])):
        text = ''
        for j in range(len(lines)):
            text = lines[j][i] + text
        text = new_text(text)
        text = text[::-1]
        for j in range(len(text)):
            new_lines[j][i] = text[j]

    lines = new_lines
    new_lines = []

    for i in range(len(lines)):
        text = lines[i]
        text = new_text(text[::-1])
        new_lines.append(text[::-1])

    lines = new_lines

    new_saw = "\n".join(lines)
    if new_saw in saw:
        print(cycle)
        result = saw[(1_000_000_000 - saw.index(new_saw)) % (cycle - saw.index(new_saw)) + saw.index(new_saw)]
        break
    saw.append(new_saw)

results = result.split("\n")
r_len = len(results)
sum = 0
for (i, line) in enumerate(results):
    sum += line.count('O') * (r_len - i)
c(sum)