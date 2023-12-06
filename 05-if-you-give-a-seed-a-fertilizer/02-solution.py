FILE_PATH = 'input.txt'
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()


class Seed:

    def __init__(self, value, seed_range):
        self.value_from = value
        self.value_to = value + seed_range - 1
        self.left = None
        self.right = None

    def copy_without_children(self):
        return Seed(self.value_from, self.value_to - self.value_from + 1)

    def merge_continuous_ranges(self):
        if self.left:
            self.left.merge_continuous_ranges()
        if self.right:
            self.right.merge_continuous_ranges()

        if self.is_left_adjacent():
            self.value_from = self.left.value_from
            self.left = self.left.left
        if self.is_right_adjacent():
            self.value_to = self.right.value_to
            self.right = self.right.right

    def is_left_adjacent(self):
        return self.left and self.left.value_to + 1 >= self.value_from

    def is_right_adjacent(self):
        return self.right and self.right.value_from - 1 <= self.value_to

    def get_all_seeds(self):
        result = []
        if self.left:
            result += self.left.get_all_seeds()
        result += [self]
        if self.right:
            result += self.right.get_all_seeds()
        return result

    def fully_contains(self, seed):
        return self.value_from <= seed.value_from and self.value_to >= seed.value_to

    def is_after(self, seed):
        return self.value_from > seed.value_to

    def is_before(self, seed):
        return self.value_to < seed.value_from

    def __str__(self):
        return '[%s   %s]' % ('{0:,}'.format(self.value_from), '{0:,}'.format(self.value_to))


class RangeTree:

    def __init__(self):
        self.root = None

    def insert(self, seed: Seed):
        if not self.root:
            self.root = seed
        else:
            current = self.root
            while True:
                if current.fully_contains(seed):
                    break
                elif current.is_after(seed):
                    if current.left:
                        current = current.left
                    else:
                        current.left = seed
                        break
                elif current.is_before(seed):
                    if current.right:
                        current = current.right
                    else:
                        current.right = seed
                        break
                else:
                    # there's some intersection so we have to split
                    if seed.value_from < current.value_from:
                        self.insert(Seed(seed.value_from, current.value_from - seed.value_from))
                    if seed.value_to > current.value_to:
                        self.insert(Seed(current.value_to + 1, seed.value_to - current.value_to))
                    break

    def merge_continuous_ranges(self):
        if self.root:
            self.root.merge_continuous_ranges()

    def get_all_nodes(self):
        if self.root:
            return self.root.get_all_seeds()
        return []

    def print(self):
        print("Tree:")
        nodes = []
        current_level = 0
        if self.root:
            nodes.append(self.root)
            self.root.level = 0
        while nodes:
            node = nodes.pop(0)
            if node.level > current_level:
                print()
                current_level = node.level
            print(node, end=" ")
            if node.left:
                node.left.level = current_level + 1
                nodes.append(node.left)
            if node.right:
                node.right.level = current_level + 1
                nodes.append(node.right)
        print('\n-------------')


class Node:

    def __init__(self, value, node_range, destination):
        self.left = None
        self.right = None
        self.value_from = int(value.strip())
        self.value_to = self.value_from + int(node_range.strip()) - 1
        self.destination = int(destination.strip())

    def __str__(self):
        return '[%s   %s] -> %s' % ('{0:,}'.format(self.value_from), '{0:,}'.format(self.value_to), '{0:,}'.format(self.destination))


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
                if value < current.value_from:
                    if current.left:
                        current = current.left
                    else:
                        current.left = node
                        return
                elif value > current.value_from:
                    if current.right:
                        current = current.right
                    else:
                        current.right = node
                        return
                else:
                    raise Exception("invalid tree")

    def find(self, seed: Seed):
        current = self.root
        while current:
            # all lower than
            if seed.value_to < current.value_from:
                if current.left:
                    current = current.left
                else:
                    return [seed.copy_without_children()]
            # all higher than
            elif seed.value_from > current.value_to:
                if current.right:
                    current = current.right
                else:
                    return [seed.copy_without_children()]
            # split
            else:
                result = []
                start = seed.value_from
                end = seed.value_to
                if start < current.value_from:
                    result += self.find(Seed(start, current.value_from - start))
                    start = current.value_from
                if end > current.value_to:
                    result += self.find(Seed(current.value_to + 1, end - current.value_to))
                    end = current.value_to
                if end - start >= 0:
                    result += [Seed(start - current.value_from + current.destination, end - start + 1)]
                return result


seeds = RangeTree()
current_from = None
current_to = None
maps = {}
for line in lines:
    if line.strip():
        if line.startswith('seeds:'):
            tmp_seeds = [int(number.strip()) for number in line.replace('seeds:', '').split(' ') if number.strip()]
            for (index, seed) in enumerate(tmp_seeds):
                if not index % 2:
                    seeds.insert(Seed(seed, tmp_seeds[index + 1]))
        elif ' map:' in line:
            mapping = line.replace(' map:', '').strip().split('-to-')
            current_from = mapping[0]
            current_to = mapping[1]
            maps[current_from] = Tree(current_from, current_to)
        else:
            (destination_start, source_start, source_range) = line.strip().split(' ')
            maps[current_from].insert(source_start, source_range, destination_start)

map = maps.get('seed')
values = seeds
values.merge_continuous_ranges()
values.print()
while map:
    print('Map %s -> %s' % (map.from_name, map.to_name))
    new_values = RangeTree()
    for seed in values.get_all_nodes():
        for new_seed in map.find(seed):
            new_values.insert(new_seed)
    new_values.merge_continuous_ranges()
    new_values.print()
    values = new_values
    map = maps.get(map.to_name)


current = values.root
while current.left:
    current = current.left
print('Result: %d' % current.value_from)
