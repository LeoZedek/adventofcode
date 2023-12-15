with open("input", "r") as file:
	data = file.readlines()

for i in range(len(data)):
	data[i] = data[i].strip()

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


north_tilted_map = [""] * len(data)

for j in range(len(data[0])):

	column = get_column(data, j)

	tilted_column = tilted(column)

	for i in range(len(tilted_column)):

		north_tilted_map[i] += tilted_column[i]

result = 0

for i in range(len(north_tilted_map)):

	height = len(north_tilted_map)

	result += (height - i) * north_tilted_map[i].count("O")

print(result)