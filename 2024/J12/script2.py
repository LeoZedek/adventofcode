RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

DIRECTIONS = [RIGHT, DOWN, LEFT, UP]

DELTAS = {
	RIGHT: (1, 0),
	DOWN: (0, 1),
	LEFT: (-1, 0),
	UP: (0, -1)
}

SIDE_DIRECTIONS = {
	RIGHT: [(0, 1), (0, -1)],
	DOWN: [(1, 0), (-1, 0)],
	LEFT: [(0, 1), (0, -1)],
	UP: [(1, 0), (-1, 0)]
}

def add_border(matrix, char, width):
	for i in range(len(matrix)):
		matrix[i] = char * width + matrix[i] + char * width

	matrix.append(char * len(matrix[0]))
	matrix.insert(0, char * len(matrix[0]))

def get_region(map, i, j):
	char = map[i][j]
	region_squares = set()

	actual_region.add((i, j))

	area, perimeter = 1, 0

	for delta in DELTAS.values():
		new_i = i + delta[0]
		new_j = j + delta[1]

		if not((new_i, new_j) in actual_region) and data[new_i][new_j] == char:
			get_region(map, new_i, new_j)

def mark_side(i, j, direction, squared_mark):
	char = data[i][j]
	delta = DELTAS[direction]
	current_i, current_j = i, j
	di, dj = i + delta[0], j + delta[1]

	for side_direction in SIDE_DIRECTIONS[direction]:

		while data[current_i][current_j] == char and data[di][dj] != char:
			squared_mark.add(((current_i, current_j), direction))
			current_i, current_j = current_i + side_direction[0], current_j + side_direction[1]
			di, dj = di + side_direction[0], dj + side_direction[1]

		current_i, current_j = i, j
		di, dj = i + delta[0], j + delta[1]

def get_number_sides(actual_region):
	sides = 0
	squared_mark = set()

	for i, j in actual_region:

		for direction, delta in DELTAS.items():
			new_i = i + delta[0]
			new_j = j + delta[1]

			if data[i][j] != data[new_i][new_j] and not(((i, j), direction) in squared_mark):
				sides += 1
				mark_side(i, j, direction, squared_mark)

	return sides

with open('input') as file:
	data = file.read().splitlines()

add_border(data, '.', 1)

visited_square = set()

r = 0

for i in range(len(data)):
	for j in range(len(data[i])):
		if data[i][j] != '.' and not((i, j) in visited_square):
			actual_region = set()
			get_region(data, i, j)
			area = len(actual_region)
			perimeter = get_number_sides(actual_region)
			visited_square = visited_square.union(actual_region)

			r += area * perimeter

print(r)