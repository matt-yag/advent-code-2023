from functools import reduce

FILE_PATH = 'input.txt'
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()

cards_counter = [1] * len(lines)
for (index, line) in enumerate(lines):
    game = line.split(':')[1].split('|')
    winning = [number.strip() for number in game[0].split(' ') if number.strip()]
    my_winning = [number.strip() for number in game[1].split(' ') if number.strip() and number.strip() in winning]
    points = len(my_winning)
    for i in range(points):
        cards_counter[index + i + 1] += cards_counter[index]

print(reduce(lambda x, y: x + y, cards_counter))
