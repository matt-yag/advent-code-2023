import re

from utils import a, o, c, aoc

lines = aoc('-2')


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
        for line in self.lines:
            if line[max(2 * i - len(line), 0):i] != line[i:min(len(line), 2 * i)][::-1]:
                return False
        return True

    def check_2(self, i):
        length = min(i + 1, len(self.lines) - i - 1)
        for j in range(0, length):
            start = j + i + 1 - length
            if self.lines[start] != self.lines[i + length - j]:
                return False
        return True


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
