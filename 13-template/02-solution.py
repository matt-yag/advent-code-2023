import re

from utils import a, o, c, aoc

lines = aoc()


def how_many_diffs(str1, str2):
    diffs = 0
    for (i, c) in enumerate(str1):
        if c != str2[i]:
            diffs += 1
            if diffs > 1:
                return diffs
    return diffs


class Pattern:

    def __init__(self, lines):
        self.lines = lines

    def __str__(self):
        return "\n".join(self.lines) + "\n\n"

    def find_reflection(self):
        for i in range(1, len(self.lines[0])):
            if self.check_1(i):
                return i

        for i in range(0, len(self.lines) - 1):
            if self.check_2(i):
                return (i + 1) * 100

        raise Exception("oo")

    def check_1(self, i):
        diffs = 0
        for line in self.lines:
            diffs += how_many_diffs(line[max(2 * i - len(line), 0):i], line[i:min(len(line), 2 * i)][::-1])
            if diffs > 1:
                return False
        return diffs == 1

    def check_2(self, i):
        diffs = 0
        length = min(i + 1, len(self.lines) - i - 1)
        for j in range(0, length):
            start = j + i + 1 - length
            diffs += how_many_diffs(self.lines[start], self.lines[i + length - j])
            if diffs > 1:
                return False
        return diffs == 1


current = []
patterns = []
for line in lines:
    if not line:
        patterns.append(Pattern(current))
        current = []
    else:
        current.append(line)
if current:
    patterns.append(Pattern(current))

sum = 0
for pattern in patterns:
    print(pattern)
    sum += pattern.find_reflection()

print(sum)
