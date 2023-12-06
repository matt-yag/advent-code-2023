FILE_PATH = 'input.txt'
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()


class Node:

    def __init__(self, value, node_range, destination):
        self.left = None
        self.right = None
        self.value = int(value.strip())
        self.range = int(node_range.strip())
        self.destination = int(destination.strip())


class Tree:

    def __init__(self, from_name, to_name):
        self.root = None
        self.from_name = from_name
        self.to_name = to_name

    def insert(self, value, node_range, destination):
        node = Node(value, node_range, destination)
        value = int(value.strip())
        if not self.root:
            self.root = node
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left:
                        current = current.left
                    else:
                        current.left = node
                        return
                elif value > current.value:
                    if current.right:
                        current = current.right
                    else:
                        current.right = node
                        return
                else:
                    raise Exception("invalid tree")

    def find(self, value):
        current = self.root
        while current:
            if current.value <= value and value - current.value < current.range:
                return value - current.value + current.destination
            elif value > current.value:
                current = current.right
            elif value < current.value:
                current = current.left
        return value


seeds = None
current_from = None
current_to = None
maps = {}
for line in lines:
    if line.strip():
        if line.startswith('seeds:'):
            seeds = [int(number.strip()) for number in line.replace('seeds:', '').split(' ') if number.strip()]
        elif ' map:' in line:
            mapping = line.replace(' map:', '').strip().split('-to-')
            current_from = mapping[0]
            current_to = mapping[1]
            maps[current_from] = Tree(current_from, current_to)
        else:
            numbers = line.strip().split(' ')
            maps[current_from].insert(numbers[1], numbers[2], numbers[0])

map = maps.get('seed')
values = seeds
while map:
    new_values = []
    for seed in values:
        new_values.append(map.find(seed))
    values = new_values
    map = maps.get(map.to_name)

print(min(values))
