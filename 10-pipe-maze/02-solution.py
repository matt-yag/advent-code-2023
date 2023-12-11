import re

from matplotlib import pyplot as plt

from utils import x, c, aoc, MatrixDrawer

NEXT = {
    '|': lambda start, previous: (start[0] - 1, start[1]) if previous == (start[0] + 1, start[1]) else (
        start[0] + 1, start[1]),
    '-': lambda start, previous: (start[0], start[1] - 1) if previous == (start[0], start[1] + 1) else (
        start[0], start[1] + 1),
    'L': lambda start, previous: (start[0] - 1, start[1]) if previous == (start[0], start[1] + 1) else (
        start[0], start[1] + 1),
    'J': lambda start, previous: (start[0], start[1] - 1) if previous == (start[0] - 1, start[1]) else (
        start[0] - 1, start[1]),
    '7': lambda start, previous: (start[0], start[1] - 1) if previous == (start[0] + 1, start[1]) else (
        start[0] + 1, start[1]),
    'F': lambda start, previous: (start[0] + 1, start[1]) if previous == (start[0], start[1] + 1) else (
        start[0], start[1] + 1),
}

lines = aoc()

(y, x) = (None, None)
for index, line in enumerate(lines):
    if line.find('S') > -1:
        (y, x) = (index, line.find('S'))


def find_next(position):
    if position[0] > 0 and lines[position[0] - 1][position[1]] in ('|', 'F', '7'):
        return (position[0] - 1, position[1])
    if position[1] > 0 and lines[position[0]][position[1] - 1] in ('F', '-', 'L'):
        return (position[0], position[1] - 1)
    if position[0] + 1 < len(lines) and lines[position[0] + 1][position[1]] in ('|', 'L', 'J'):
        return (position[0] + 1, position[1])
    if position[1] + 1 < len(lines[0]) and lines[position[0]][position[1] + 1] in ('-', 'J', '7'):
        return (position[0], position[1] + 1)


def can_go_down(x, y):
    return y + 1 < len(lines) and lines[y + 1][x] in ('|', 'L', 'J')


def can_go_up(x, y):
    return y > 0 and lines[y - 1][x] in ('|', 'F', '7')


def can_go_left(x, y):
    return x > 0 and lines[y][x - 1] in ('-', 'F', 'L')


def can_go_right(x, y):
    return x + 1 < len(lines[0]) and lines[y][x + 1] in ('-', '7', 'J')


def calculate_sign(x, y):
    if can_go_down(x, y) and can_go_up(x, y):
        return '|'
    if can_go_left(x, y) and can_go_right(x, y):
        return '-'
    if can_go_down(x, y) and can_go_right(x, y):
        return 'F'
    if can_go_down(x, y) and can_go_left(x, y):
        return '7'
    if can_go_up(x, y) and can_go_left(x, y):
        return 'J'
    if can_go_up(x, y) and can_go_right(x, y):
        return 'L'


lines[y] = lines[y].replace('S', calculate_sign(x, y))

for line in lines:
    print(line)

prev = (y, x)
current = find_next(prev)
path = [prev, current]
while current != (y, x):
    next = NEXT[lines[current[0]][current[1]]](current, prev)
    path.append(next)
    prev = current
    current = next

only_main_lines = []
for (i, line) in enumerate(lines):
    string = ''
    for (j, char) in enumerate(line):
        if (i, j) in path:
            string += char
        else:
            string += '.'
    only_main_lines.append(string)

print('------- Updated -------')
for line in only_main_lines:
    print(line)

drawer = MatrixDrawer(only_main_lines)

# 9 - don't know
# 4 - pipeline
result = [['9' for _ in range(len(only_main_lines[0]))] for _ in range(len(only_main_lines))]
for point in path:
    result[point[0]][point[1]] = '4'


def can_explore_up(y, x, squeeze_direction_y, squeeze_direction_x):
    if y == 0:
        return False, None
    if only_main_lines[y - 1][x] == '-':
        return False, None

    if only_main_lines[y][x] == '-' and squeeze_direction_y == 'B':
        return False, None

    if only_main_lines[y][x] == 'F' and squeeze_direction_y == 'B' and squeeze_direction_x == 'R':
        return False, None

    if only_main_lines[y][x] == '7' and squeeze_direction_y == 'B' and squeeze_direction_x == 'L':
        return False, None

    if squeeze_direction_x == 'R' and only_main_lines[y - 1][x] == 'F':
        return False, None

    if squeeze_direction_x == 'L' and only_main_lines[y - 1][x] == '7':
        return False, None

    # print('Can I go up?', y, x, squeeze_direction)
    if only_main_lines[y - 1][x] == 'L' or (only_main_lines[y][x] == 'L' and squeeze_direction_y == 'B') or (
            only_main_lines[y][x] == 'J' and squeeze_direction_y == 'T'):
        return True, 'L'

    if only_main_lines[y - 1][x] == 'J' or (only_main_lines[y][x] == 'L' and squeeze_direction_y == 'T') or (
            only_main_lines[y][x] == 'J' and squeeze_direction_y == 'B'):
        return True, 'R'

    return True, squeeze_direction_x


def can_explore_down(y, x, squeeze_direction_y, squeeze_direction_x):
    if y + 1 == len(only_main_lines):
        return False, None
    if only_main_lines[y + 1][x] == '-':
        return False, None

    if only_main_lines[y][x] == '-' and squeeze_direction_y in ('T',):
        return False, None

    if only_main_lines[y][x] == 'L' and (squeeze_direction_y == 'T' and squeeze_direction_x == 'R'):
        return False, None

    if only_main_lines[y][x] == 'J' and (squeeze_direction_y == 'T' and squeeze_direction_x == 'L'):
        return False, None

    if squeeze_direction_x == 'R' and only_main_lines[y + 1][x] == 'L':
        return False, None

    if squeeze_direction_x == 'L' and only_main_lines[y + 1][x] == 'J':
        return False, None

    # print('Can I go down?', y, x, squeeze_direction_y, squeeze_direction_x)
    if only_main_lines[y + 1][x] == 'F' or (only_main_lines[y][x] == 'F' and squeeze_direction_y == 'T') or (
            only_main_lines[y][x] == '7' and squeeze_direction_y == 'B'):
        return True, 'L'

    if only_main_lines[y + 1][x] == '7' or (only_main_lines[y][x] == 'F' and squeeze_direction_y == 'B') or (
            only_main_lines[y][x] == '7' and squeeze_direction_y == 'T'):
        return True, 'R'

    return True, squeeze_direction_x


def can_explore_right(y, x, squeeze_direction_y, squeeze_direction_x):
    if x + 1 == len(only_main_lines[0]):
        return False, None
    if only_main_lines[y][x + 1] == '|':
        return False, None

    if only_main_lines[y][x] == '|' and squeeze_direction_x in ('L',):
        return False, None

    if only_main_lines[y][x] == '7' and (squeeze_direction_y == 'B' and squeeze_direction_x == 'L'):
        return False, None

    if only_main_lines[y][x] == 'J' and (squeeze_direction_y == 'T' and squeeze_direction_x == 'L'):
        return False, None

    if squeeze_direction_y == 'T' and only_main_lines[y][x + 1] == 'J':
        return False, None

    if squeeze_direction_y == 'B' and only_main_lines[y][x + 1] == '7':
        return False, None

    # print('Can I go right?', y, x, squeeze_direction)
    if only_main_lines[y][x + 1] == 'F' or (only_main_lines[y][x] == 'L' and squeeze_direction_x == 'R') or (
            only_main_lines[y][x] == 'F' and squeeze_direction_x == 'L'):
        return True, 'T'

    if only_main_lines[y][x + 1] == 'L' or (only_main_lines[y][x] == 'L' and squeeze_direction_x == 'L') or (
            only_main_lines[y][x] == 'F' and squeeze_direction_x == 'R'):
        return True, 'B'

    return True, squeeze_direction_y


def can_explore_left(y, x, squeeze_direction_y, squeeze_direction_x):
    if x == 0:
        return False, None

    if only_main_lines[y][x - 1] == '|':
        return False, None

    if only_main_lines[y][x] == '|' and squeeze_direction_x in ('R',):
        return False, None

    if only_main_lines[y][x] == 'F' and (squeeze_direction_y == 'B' and squeeze_direction_x == 'R'):
        return False, None

    if only_main_lines[y][x] == 'L' and (squeeze_direction_y == 'T' and squeeze_direction_x == 'R'):
        return False, None

    if squeeze_direction_y == 'T' and only_main_lines[y][x - 1] == 'L':
        return False, None

    if squeeze_direction_y == 'B' and only_main_lines[y][x - 1] == 'F':
        return False, None

    # print('Can I go left?', y, x, squeeze_direction)
    if only_main_lines[y][x - 1] == '7' or (only_main_lines[y][x] == '7' and squeeze_direction_x == 'R') or (
            only_main_lines[y][x] == 'J' and squeeze_direction_x == 'L'):
        return True, 'T'

    if only_main_lines[y][x - 1] == 'J' or (only_main_lines[y][x] == 'J' and squeeze_direction_x == 'R') or (
            only_main_lines[y][x] == '7' and squeeze_direction_x == 'L'):
        return True, 'B'

    return True, squeeze_direction_y


ax = drawer.show()


def explore(y, x, visited, squeeze_direction_y, squeeze_direction_x, from_str):
    to_explore = []
    to_explore.append((y, x, visited, squeeze_direction_y, squeeze_direction_x, from_str))

    while to_explore:
        (y, x, visited, squeeze_direction_y, squeeze_direction_x, from_str) = to_explore.pop(0)

        if (y, x) in visited[-1]:
            continue

        if from_str != 'starting point':
            drawer.draw_line_between_cells(ax, y, x, from_str['y'], from_str['x'],
                                           (squeeze_direction_x or '') + (squeeze_direction_y or ''),
                                           (from_str['dy'] or '') + (from_str['dx'] or ''))

        #print('Go %s -> (%s, %s) from %s%s' % (from_str, y, x, squeeze_direction_y, squeeze_direction_x))
        visited[-1].append((y, x))
        (up, new_squeeze) = can_explore_up(y, x, squeeze_direction_y, squeeze_direction_x)
        if up:
            to_explore.append((y - 1, x, visited, 'B', new_squeeze,
                    {'y': y, 'x': x, 'dy': squeeze_direction_y, 'dx': squeeze_direction_x}))
        (down, new_squeeze) = can_explore_down(y, x, squeeze_direction_y, squeeze_direction_x)
        if down:
            to_explore.append((y + 1, x, visited, 'T', new_squeeze,
                    {'y': y, 'x': x, 'dy': squeeze_direction_y, 'dx': squeeze_direction_x}))

        (left, new_squeeze) = can_explore_left(y, x, squeeze_direction_y, squeeze_direction_x)
        if left:
            to_explore.append((y, x - 1, visited, new_squeeze, 'R',
                    {'y': y, 'x': x, 'dy': squeeze_direction_y, 'dx': squeeze_direction_x}))

        (right, new_squeeze) = can_explore_right(y, x, squeeze_direction_y, squeeze_direction_x)
        if right:
            to_explore.append((y, x + 1, visited, new_squeeze, 'L',
                    {'y': y, 'x': x, 'dy': squeeze_direction_y, 'dx': squeeze_direction_x}))


for i in range(len(only_main_lines)):
    for j in range(len(only_main_lines[i])):
        if result[i][j] == 9:
            if i == 0 or i + 1 == len(only_main_lines):
                result[i][j] = 1
            if j == 0 or j + 1 == len(only_main_lines[i]):
                result[i][j] = 1

visited = []


def is_visited(y, x):
    for v in visited:
        if (y, x) in v:
            return True
    return False


for i in range(len(only_main_lines)):
    for j in range(len(only_main_lines[i])):
        if not is_visited(i, j) and only_main_lines[i][j] == '.':
            visited.append([])
            print('------ Start explore -------')
            explore(i, j, visited, None, None, 'starting point')
            print('------ End explore -------')



print('------- Visited -------')


def is_free(v):
    for position in v:
        if position[0] == 0 or position[1] == 0 or position[0] + 1 == len(only_main_lines) or position[1] + 1 == len(
                only_main_lines[0]):
            return True
    return False


sum = 0
for v in visited:
    if not is_free(v):
        for position in v:
            if result[position[0]][position[1]] == '9':
                sum += 1
                result[position[0]][position[1]] = '7'

print('------- Result -------')
for line in result:
    print(''.join(line))

print(sum)

plt.show()