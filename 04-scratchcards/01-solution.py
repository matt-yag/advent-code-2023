FILE_PATH = 'input.txt'
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()

points = 0
for line in lines:
    game = line.split(':')[1].split('|')
    winning = [number.strip() for number in game[0].split(' ') if number.strip()]
    my_winning = [number.strip() for number in game[1].split(' ') if number.strip() and number.strip() in winning]
    points += (1 << len(my_winning) - 1) if my_winning else 0

print(points)