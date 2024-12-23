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

DELTAS = {
	RIGHT: (0, 1),
	LEFT: (0, -1),
	DOWN: (1, 0),
	UP: (-1, 0)
}

_map = []
orders = ''

with open('input') as file:
	row = file.readline()
	while row != '\n':
		_map.append(list(row))
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

for order in orders:
	direction = DIRECTIONS[order]

	delta = DELTAS[direction]
	d_row, d_col = delta
	if _map[robot_row + d_row][robot_col + d_col] == '.':
		robot_row, robot_col = robot_row + d_row, robot_col + d_col
	elif _map[robot_row + d_row][robot_col + d_col] == 'O':
		i = 1
		while _map[robot_row + i*d_row][robot_col + i*d_col] == 'O':
			i += 1
		if _map[robot_row + i*d_row][robot_col + i*d_col] == '.':
			_map[robot_row + i*d_row][robot_col + i*d_col] = 'O'
			_map[robot_row + d_row][robot_col + d_col] = '.'
			robot_row, robot_col = robot_row + d_row, robot_col + d_col

r = 0

for i in range(len(_map)):
	for j in range(len(_map[i])):
		if _map[i][j] == 'O':
			r += 100 * i + j

print(r)
