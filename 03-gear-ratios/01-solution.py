# cat input-test.txt| sed -r -e 's/[0-9.]/0/g' | sed -r -e 's/[^0]/1/g' > sign-mask-test.txt
import re
from functools import reduce

INPUT_PATH = 'input.txt'
with open(INPUT_PATH, 'r') as file:
    lines = file.readlines()


class EngineSchematic:
    numbers = []

    def __init__(self, lines):
        self.sign_mask = [0] * (len(lines) + 2)
        for (index, line) in enumerate(lines):
            mask = ('0' + re.sub(r'[^0]', '1', re.sub(r'[0-9.]', '0', line.strip())) + '0')[::-1]
            self.sign_mask[index + 1] = int(mask, 2)
            matches = re.finditer(r'[0-9]+', line)
            self.numbers += [Number(index + 1, match.start() + 1, match.group()) for match in matches]

    def all_valid_number(self):
        return [number.value for number in self.numbers if self.__is_valid(number)]

    def __is_valid(self, number):
        return (self.sign_mask[number.line_number - 1] | self.sign_mask[number.line_number] | self.sign_mask[
            number.line_number + 1]) & number.coverage_mask()


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


engine = EngineSchematic(lines)
print(reduce(lambda x, y: x + y, engine.all_valid_number()))
