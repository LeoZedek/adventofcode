UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3

CONNECT_SOUTH = set(['|', '7', 'F'])
CONNECT_NORTH = set(['L', '|', 'J'])
CONNECT_EAST = set(['-', 'L', 'F'])
CONNECT_WEST = set(['-', 'J', '7'])

COME_FROM = {
	UP: DOWN,
	DOWN: UP,
	LEFT: RIGHT,
	RIGHT: LEFT
}

PIPES_DIRECTIONS = {
	'|': [UP, DOWN],
	'7': [DOWN, LEFT],
	'-': [LEFT, RIGHT],
	'L': [UP, RIGHT],
	'J': [UP, LEFT],
	'F': [DOWN, RIGHT]
}

def find_direction_loop(_map, pos):

	x = pos[1]
	y = pos[0]

	result = []

	if x - 1 > 0 and _map[y][x-1] in CONNECT_EAST:
		result.append(LEFT)

	if x + 1 < len(_map[0]) and _map[y][x+1] in CONNECT_WEST:
		result.append(RIGHT)

	if y - 1 > 0 and _map[y-1][x] in CONNECT_SOUTH:
		result.append(UP)

	if y + 1 < len(_map) and _map[y+1][x] in CONNECT_NORTH:
		result.append(DOWN)

	return result

def go(_map, pos, direction):

	x = pos[1]
	y = pos[0]

	if direction == UP:
		new_x = x
		new_y = y - 1

	elif direction == DOWN:
		new_x = x
		new_y = y + 1
	elif direction == LEFT:
		new_x = x - 1
		new_y = y
	elif direction == RIGHT:
		new_x = x + 1
		new_y = y

	pipe = _map[new_y][new_x]

	if pipe == 'S':
		return (new_y, new_x), None
	
	possible_new_directions = PIPES_DIRECTIONS[pipe].copy()
	possible_new_directions.remove(COME_FROM[direction])

	new_direction = possible_new_directions[0]

	return (new_y, new_x), new_direction

def is_inside_path(_map, path, pos):
	x = pos[1]
	y = pos[0]

	new_x = x + 1

	border_cross = 0

	while new_x < len(_map[y]):
		if (y, new_x) in path:

			border = _map[y][new_x]

			if border == '|':
				border_cross += 1

			elif border == 'L' or border == 'F':
				first_border = border

				while _map[y][new_x] != 'J' and _map[y][new_x] != '7':
					new_x += 1

				if (first_border == 'L' and _map[y][new_x] == '7') or (first_border == 'F' and _map[y][new_x] == 'J'):
					border_cross += 1

		new_x += 1

	if border_cross % 2 == 0:
		return False
	else:
		return True

with open("input", "r") as file:
	data = file.readlines()

# Remove the last char '\n'
for i in range(len(data)):
	data[i] = data[i].strip()

_map = data

for i in range(len(_map)):
	for j in range(len(_map[i])):

		if _map[i][j] == 'S':
			animal_pos = (i, j)

whole_path = set([animal_pos])

current_position = animal_pos

possible_directions = find_direction_loop(_map, animal_pos)

for pipe, directions in PIPES_DIRECTIONS.items():
	if possible_directions[0] in directions and possible_directions[1] in directions:
		start_pipe = pipe

direction = possible_directions[0]

current_position, direction = go(_map, current_position, direction)

step = 1

while current_position != animal_pos:
	whole_path.add(current_position)

	current_position, direction = go(_map, current_position, direction)

	step += 1

_map[animal_pos[0]] = _map[animal_pos[0]].replace("S", start_pipe)

result = 0

for i in range(len(_map)):
	for j in range(len(_map[i])):

		pos = (i, j)

		if not(pos in whole_path) and is_inside_path(_map, whole_path, pos):
			result += 1

print(result)