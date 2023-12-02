from functools import reduce

FILE_PATH = 'input.txt'
MAX = {
    'red': 12,
    'green': 13,
    'blue': 14
}
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()


class Game:

    def __init__(self, line):
        (game, cubes) = line.split(': ')
        self.number = int(game.replace('Game ', ''))
        self.subgames = [Subgame(subgame) for subgame in cubes.split('; ')]

    def is_valid(self):
        return all(subgame.is_valid() for subgame in self.subgames)

    def get_power(self):
        red = 1
        green = 1
        blue = 1
        for subgame in self.subgames:
            red = subgame.get_red_if_higher(red)
            green = subgame.get_green_if_higher(green)
            blue = subgame.get_blue_if_higher(blue)
        return red * green * blue


class Subgame:

    def __init__(self, line):
        cubes = line.split(', ')
        self.cubes = {}
        for cube in cubes:
            (amount, category) = cube.split(' ')
            self.cubes[category.strip()] = int(amount)

    def is_valid(self):
        for (category, max_count) in MAX.items():
            if self.cubes.get(category, 0) > max_count:
                return False
        return True

    def get_red_if_higher(self, current):
        return self.get_if_higher('red', current)

    def get_blue_if_higher(self, current):
        return self.get_if_higher('blue', current)

    def get_green_if_higher(self, current):
        return self.get_if_higher('green', current)

    def get_if_higher(self, category, current):
        return max(self.cubes.get(category, 1), current)


games = []
for line in lines:
    games.append(Game(line))

print(reduce(lambda power1, power2: power1 + power2, [game.get_power() for game in games]))
