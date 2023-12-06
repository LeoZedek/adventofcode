RIGHT = 0
LEFT = 1
DOWN = 2
UP = 3

directions = [RIGHT, DOWN, LEFT, UP]

with open('input') as f:

	data = list(map(lambda x : x.split('\n')[0], f.readlines()))

my_map = []

index = 0

construct_map = True

while construct_map:
	my_map.append(data[index])

	index += 1

	if len(data[index]) == 0:
		construct_map = False

instructions_string = data[index + 1]

instructions = []

memo_digit = ""

for char in instructions_string:

	if not(char.isdigit()):
		if len(memo_digit) > 0:
			instructions.append(int(memo_digit))
		instructions.append(char)
		memo_digit = ""

	else:
		memo_digit += char

if len(memo_digit) > 0:
	instructions.append(int(memo_digit))

def is_at_edge(my_map, my_position, direction):
	row = my_position[0] - 1
	column = my_position[1] - 1

	if direction == RIGHT:
		new_column = column + 1
		return new_column >= len(my_map[row]) or my_map[row][new_column] == " "

	if direction == LEFT:
		new_column = column - 1
		return new_column < 0 or my_map[row][new_column] == " "

	if direction == UP:
		new_row = row - 1
		return new_row < 0 or column >= len(my_map[new_row]) or my_map[new_row][column] == " "

	if direction == DOWN:
		new_row = row + 1
		return new_row >= len(my_map) or column >= len(my_map[new_row]) or my_map[new_row][column] == " "

def next_case(my_map, my_position, direction):

	row = my_position[0] - 1
	column = my_position[1] - 1

	if is_at_edge(my_map, my_position, direction):
		if direction == RIGHT:
			j = column
			while j - 1 >= 0 and my_map[row][j - 1] != " ":
				j -= 1

			return my_map[row][j]

		if direction == LEFT:
			j = column

			while j + 1 < len(my_map[row]) and my_map[row][j + 1] != " ":
				j += 1

			return my_map[row][j]

		if direction == DOWN:
			i = row

			while i - 1 >= 0 and column < len(my_map[i - 1]) and my_map[i - 1][column] != " ":
				i -= 1

			return my_map[i][column]

		if direction == UP:
			i = row

			while i + 1 < len(my_map) and column < len(my_map[i + 1]) and my_map[i + 1][column] != " ":
				i += 1

			return my_map[i][column]

	else:
		new_row = row
		new_column = column

		new_row += (direction == UP) * -1 + (direction == DOWN) * 1
		new_column += (direction == LEFT) * -1 + (direction == RIGHT) * 1

		return my_map[new_row][new_column]

def move(my_map, my_position, direction):

	row = my_position[0] - 1
	column = my_position[1] - 1

	if is_at_edge(my_map, my_position, direction):
		if direction == RIGHT:
			j = column
			while j - 1 >= 0 and my_map[row][j - 1] != " ":
				j -= 1

			return (row + 1, j + 1)

		if direction == LEFT:
			j = column

			while j + 1 < len(my_map[row]) and my_map[row][j + 1] != " ":
				j += 1

			return (row + 1, j + 1)

		if direction == DOWN:
			i = row

			while i - 1 >= 0 and column < len(my_map[i - 1]) and my_map[i - 1][column] != " ":
				i -= 1

			return (i + 1, column + 1)

		if direction == UP:
			i = row

			while i + 1 < len(my_map) and column < len(my_map[i + 1]) and my_map[i + 1][column] != " ":
				i += 1

			return (i + 1, column + 1)

	else:
		new_row = row
		new_column = column

		new_row += (direction == UP) * -1 + (direction == DOWN) * 1
		new_column += (direction == LEFT) * -1 + (direction == RIGHT) * 1

		return (new_row + 1, new_column + 1)

for j, char in enumerate(my_map[0]):

	if char == ".":
		my_position = (1, j + 1)
		break

my_direction = RIGHT

for instruction in instructions:

	if isinstance(instruction, str):
		if instruction == "R":
			my_direction = directions[(directions.index(my_direction) + 1) % len(directions)]

		else:
			my_direction = directions[(directions.index(my_direction) - 1) % len(directions)]

	else:

		number_pas = instruction

		while number_pas > 0 and next_case(my_map, my_position, my_direction) != "#":
			number_pas -= 1
			my_position = move(my_map, my_position, my_direction)


value_direction = {
	RIGHT : 0,
	DOWN : 1,
	LEFT : 2,
	UP : 3
}

print(1000 * my_position[0] + 4 * my_position[1] + value_direction[my_direction])
