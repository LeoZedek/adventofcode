def is_column_empty(_map, column):

	for i in range(len(_map)):
		if _map[i][column] == '#':
			return False

	return True

EXPANSION = 1000000 - 1

with open("input", "r") as file:

	data = file.readlines()

# Removing the '\n'
for i in range(len(data)):
	data[i] = data[i].strip()

empty_lines = []
empty_columns = []

for i in range(len(data)):
	if data[i].count('#') == 0:
		empty_lines.append(i)

for j in range(len(data[0])):
	if is_column_empty(data, j):
		empty_columns.append(j)

galaxies = []

number_empty_lines_encountered = 0

for i in range(len(data)):

	if i in empty_lines:
		number_empty_lines_encountered += 1

	else:

		number_empty_columns_encountered = 0
		for j in range(len(data[i])):

			if j in empty_columns:
				number_empty_columns_encountered += 1

			else:

				if data[i][j] == '#':
					galaxies.append((i + number_empty_lines_encountered * EXPANSION, j + number_empty_columns_encountered * EXPANSION))

result = 0

for i in range(len(galaxies)):
	galaxy1 = galaxies[i]

	for k in range(i + 1, len(galaxies)):
		galaxy2 = galaxies[k]

		result += abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])

print(result)