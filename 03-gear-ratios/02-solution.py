# cat input-test.txt| sed -r -e 's/[0-9.]/0/g' | sed -r -e 's/[^0]/1/g' > sign-mask-test.txt
import re
from functools import reduce

INPUT_PATH = 'input.txt'
with open(INPUT_PATH, 'r') as file:
    lines = file.readlines()


class EngineSchematic:

    def __init__(self, lines):
        self.sign_mask = []
        self.numbers = [[]] * (len(lines) + 2)
        for (index, line) in enumerate(lines):
            matches = re.finditer(r'[*]', line)
            self.sign_mask += [Mask(index + 1, match.start() + 1) for match in matches]
            matches = re.finditer(r'[0-9]+', line)
            self.numbers[index + 1] = [Number(index + 1, match.start() + 1, match.group()) for match in matches]

    def all_gears(self):
        gears = []
        for mask in self.sign_mask:
            if mask:
                numbers = [number.value for number in
                           (self.numbers[mask.line_number - 1] + self.numbers[mask.line_number] + self.numbers[
                               mask.line_number + 1]) if number.coverage_mask() & mask.coverage_mask()]
                if len(numbers) == 2:
                    gears.append(numbers[0] * numbers[1])
        return gears


class Number:

    def __init__(self, line_number, position, value):
        self.line_number = line_number
        self.position = position
        self.length = len(value)
        self.value = int(value)

    def __str__(self):
        return '%s (%s) (%s, %s)' % (self.value, self.length, self.line_number, self.position)

    def coverage_mask(self):
        return int('1' * (self.length + 2) + '0' * (self.position - 1), 2)


class Mask:

    def __init__(self, line_number, position):
        self.line_number = line_number
        self.position = position

    def coverage_mask(self):
        return int('1' + '0' * self.position, 2)


engine = EngineSchematic(lines)
print(reduce(lambda x, y: x + y, engine.all_gears()))
