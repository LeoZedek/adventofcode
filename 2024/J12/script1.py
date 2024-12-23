DELTAS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

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

	for delta in DELTAS:
		new_i = i + delta[0]
		new_j = j + delta[1]

		if not((new_i, new_j) in actual_region) and data[new_i][new_j] == char:
			get_region(map, new_i, new_j)

def get_perimeter(actual_region):
	perimeter = 0
	for i, j in actual_region:

		for delta in DELTAS:
			new_i = i + delta[0]
			new_j = j + delta[1]

			if data[i][j] != data[new_i][new_j]:
				perimeter += 1

	return perimeter

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
			perimeter = get_perimeter(actual_region)
			visited_square = visited_square.union(actual_region)

			r += area * perimeter

print(r)