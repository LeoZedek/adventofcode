RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

DIRECTIONS = {
	'>': RIGHT,
	'<': LEFT,
	'v': DOWN,
	'^': UP
}

HORIZONTAL = {RIGHT, LEFT}
VERTICAL = {UP, DOWN}

DELTAS = {
	RIGHT: (0, 1),
	LEFT: (0, -1),
	DOWN: (1, 0),
	UP: (-1, 0)
}

BOX = {'[', ']'}

def create_row(row):
	new_row = []
	for char in row:
		if char == '#':
			new_row.append('#')
			new_row.append('#')
		elif char == '.':
			new_row.append('.')
			new_row.append('.')
		elif char == 'O':
			new_row.append('[')
			new_row.append(']')
		elif char == '@':
			new_row.append('@')
			new_row.append('.')

	return new_row

def can_push(robot_row, robot_col, direction):
	if direction in HORIZONTAL:
		new_j = robot_col + (1 if direction == RIGHT else -1)
		while _map[robot_row][new_j] in BOX:
			new_j += 1 if direction == RIGHT else -1

		return _map[robot_row][new_j] == '.'

	elif direction in VERTICAL:
		new_i = robot_row + (1 if direction == DOWN else -1)
		col_to_push = {robot_col}
		if _map[new_i][robot_col] == '[':
			col_to_push.add(robot_col + 1)
		else:
			col_to_push.add(robot_col - 1)

		while 1:
			all_empty = True
			next_col_to_push = set()
			for col in col_to_push:
				if _map[new_i][col] == '#':
					return False
				if _map[new_i][col] != '.':
					all_empty = False
					if _map[new_i][col] == '[':
						next_col_to_push.add(col + 1)
						next_col_to_push.add(col)
					else:
						next_col_to_push.add(col - 1)
						next_col_to_push.add(col)

			col_to_push = next_col_to_push

			if all_empty:
				return True
			new_i += 1 if direction == DOWN else -1

	else:
		print('Should not happen')

def push_box(box_row, box_col, direction):
	if direction in HORIZONTAL:
		new_j = box_col + (1 if direction == RIGHT else -1)
		if _map[box_row][new_j] in BOX:
			push_box(box_row, new_j, direction)
		_map[box_row][new_j] = _map[box_row][box_col]
		_map[box_row][box_col] = '.'

	elif direction in VERTICAL:
		col_to_push = {box_col}
		if _map[box_row][box_col] == '[':
			col_to_push.add(box_col + 1)
		else:
			col_to_push.add(box_col - 1)
		new_i = box_row + (1 if direction == DOWN else -1)

		for col in col_to_push:
			if _map[new_i][col] in BOX:
				push_box(new_i, col, direction)

			_map[new_i][col] = _map[box_row][col]
			_map[box_row][col] = '.'

_map = []
orders = ''

with open('input') as file:
	row = file.readline()
	while row != '\n':
		_map.append(create_row(row))
		row = file.readline()

	row = file.readline()
	while row != '':
		orders += row[:-1]
		row = file.readline()

for i in range(len(_map)):
	for j in range(len(_map[i])):
		if _map[i][j] == '@':
			robot_row, robot_col = i, j
			_map[i][j] = '.'

def print_map():
	r = []

	for (i, row) in enumerate(_map):
		if i == robot_row:
			row = list(''.join(row))
			row[robot_col] = '@'
		print(''.join(row)) 

for order in orders:
	direction = DIRECTIONS[order]

	delta = DELTAS[direction]
	d_row, d_col = delta
	if _map[robot_row + d_row][robot_col + d_col] == '.':
		robot_row, robot_col = robot_row + d_row, robot_col + d_col
	elif _map[robot_row + d_row][robot_col + d_col] in BOX:
		if can_push(robot_row, robot_col, direction):
			push_box(robot_row + d_row, robot_col + d_col, direction)
			robot_row, robot_col = robot_row + d_row, robot_col + d_col

r = 0

for i in range(len(_map)):
	for j in range(len(_map[i])):
		if _map[i][j] == '[':
			r += 100 * i + j

print(r)
