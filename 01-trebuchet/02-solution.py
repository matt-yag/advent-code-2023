import re

FILE_PATH = 'input.txt'
TOKENS = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    r'([1-9])': 0,
}

with open(FILE_PATH, 'r') as file:
    lines = file.readlines()

sum = 0
for line in lines:
    value_min = 0
    value_max = 0
    result_min = -1
    result_max = -1
    for token in TOKENS.keys():
        match = re.search(token, line)
        if match and (result_min == -1 or result_min > match.start()):
            result_min = match.start()
            value_min = int(match.group(1)) if match.groups() else TOKENS[token]
        reversed_token = token if token.startswith(r'(') else token[::-1]
        match = re.search(reversed_token, line[::-1])
        if match and (result_max == -1 or result_max > match.start()):
            result_max = match.start()
            value_max = int(match.group(1)) if match.groups() else TOKENS[token]
    sum += value_min * 10 + value_max

print(sum)
