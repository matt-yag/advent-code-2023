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

boxes = []
for i in range(256):
    boxes.append([])


values = lines[0].split(',')
for line in values:
    if '-' in line:
        label = line[:line.index('-')]
        box = h(label)
        for (i, element) in enumerate(boxes[box]):
            if element.startswith(label + ' '):
                boxes[box].pop(i)
    elif '=' in line:
        (label, number) = line.split('=')
        box = h(label)
        found = False
        for (i, element) in enumerate(boxes[box]):
            if element.startswith(label + ' '):
                boxes[box][i] = label + ' ' + number
                found = True
        if not found:
            boxes[box].append(label + ' ' + number)
    else:
        raise Exception("oo")

sum = 0
for (j,box) in enumerate(boxes):
    for (i, l) in enumerate(box):
        print(l)
        sum += (j+1) * (i+1) * int(l.split(' ')[1])
c(sum)