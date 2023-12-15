NORTH = 0
SOUTH = 1
EAST = 2
WEST = 3

with open("input", "r") as file:
	data = file.readlines()

for i in range(len(data)):
	data[i] = data[i].strip()

def reverse(string):
	return string[::-1]

def get_column(mat, column_index):
	column = []

	for i in range(len(mat)):
		column.append(mat[i][column_index])

	return column

def tilted(line):

	free_space_index = 0

	index_rocks = []

	for i in range(len(line)):

		char = line[i]

		if char == "#":
			free_space_index = i + 1

		elif char == "O":
			index_rocks.append(free_space_index)
			free_space_index += 1

	result = []

	for i in range(len(line)):

		char = line[i]

		if char == "#":
			result.append("#")
		elif i in index_rocks:
			result.append("O")
		else:
			result.append(".")

	return "".join(result)

def tilte_map(_map, direction):

	if direction == NORTH:
		result = [""] * len(_map)

		for j in range(len(_map[0])):

			column = get_column(_map, j)

			tilted_column = tilted(column)

			for i in range(len(tilted_column)):
				result[i] += tilted_column[i]

	elif direction == SOUTH:
		result = [""] * len(_map)

		for j in range(len(_map[0])):

			column = get_column(_map, j)

			tilted_column = tilted(reverse(column))

			tilted_column = reverse(tilted_column)

			for i in range(len(tilted_column)):
				result[i] += tilted_column[i]

	elif direction == EAST:

		result = []

		for i in range(len(_map)):

			line = _map[i]

			tilted_line = tilted(reverse(line))

			tilted_line = reverse(tilted_line)

			result.append(tilted_line)

	elif direction == WEST:

		result = []

		for i in range(len(_map)):

			line = _map[i]

			tilted_line = tilted(line)

			result.append(tilted_line)

	else:
		print("should not happen")
		result = []

	return result

def cycle(_map):

	result = tilte_map(_map, NORTH)
	result = tilte_map(result, WEST)
	result = tilte_map(result, SOUTH)
	result = tilte_map(result, EAST)

	return result

def calcul_score(_map):

	result = 0

	height = len(_map)

	for i in range(len(_map)):
		result += (height - i) * _map[i].count("O")

	return result

memo = {}
order = {}
score_map = {}

temp = data

for i in range(1000):
	temp = cycle(temp)

	key = ";".join(temp)

	if key in memo:
		start_cycle = order[key]
		break
	else:
		score = calcul_score(temp)
		memo[key] = score
		order[key] = i
		score_map[i] = score

print(score_map[(1000000000 - start_cycle) % (len(memo) - start_cycle) + start_cycle - 1])
