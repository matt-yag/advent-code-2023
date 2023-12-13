import re

from utils import a, o, c, aoc

lines = aoc()


memory = {}

class Row:

    def __init__(self, line):
        line_split = line.split(' ')
        self.string = line_split[0]
        self.numbers = [int(number) for number in line_split[1].split(',')]

    @staticmethod
    def how_many(string, numbers):
        key = string + '_'.join([str(number) for number in numbers])
        if key in memory:
            return memory[key]
        size = 0
        #print(string, numbers)
        for (index, c) in enumerate(string):
            if c == '.':
                if size == 0:
                    continue
                else:
                    if numbers and size == numbers[0]:
                        numbers.pop(0)
                        size = 0
                    else:
                        memory[key] = 0
                        return 0
            elif c == '#':
                size += 1
            elif c == '?':
                if size > 0:
                    if len(numbers):
                        if size == numbers[0]:
                            numbers.pop(0)
                            size = 0
                        elif size < numbers[0]:
                            size += 1
                        else:
                            memory[key] = 0
                            return 0
                    else:
                        memory[key] = 0
                        return 0
                else:
                    result = Row.how_many('.' + string[index + 1:], list(numbers)) + Row.how_many(
                        '#' + string[index + 1:], list(numbers))
                    memory[key] = result
                    return result
            else:
                raise Exception('something wrong')
        #print('End', size, numbers)
        if len(numbers) == 1 and size == numbers[0] or len(numbers) == 0 and size == 0:
            memory[key] = 1
            return 1
        memory[key] = 0
        return 0


rows = [Row(line) for line in lines]
c(a([Row.how_many(row.string, row.numbers) for row in rows]))
