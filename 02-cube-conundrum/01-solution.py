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


games = []
for line in lines:
    games.append(Game(line))

print(reduce(lambda id1, id2: id1 + id2, [game.number for game in games if game.is_valid()]))
