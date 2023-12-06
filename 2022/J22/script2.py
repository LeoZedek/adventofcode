RIGHT = 0
LEFT = 1
DOWN = 2
UP = 3

directions = [RIGHT, DOWN, LEFT, UP]

top_left = {
	"A" : (0, 50),
	"B" : (0, 100),
	"C" : (50, 50),
	"D" : (100, 50),
	"E" : (100, 0),
	"F" : (150, 0)
}

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

def face(my_position):
	row = my_position[0] - 1
	column = my_position[1] - 1

	if row < 50:
		if column >= 100:
			return "B"
		else:
			return "A"

	elif row < 100:
		return "C"

	elif row < 150:
		if column < 50:
			return "E"
		else:
			return "D"

	else:
		return "F"

def move(my_map, my_position, direction):

	row = my_position[0] - 1
	column = my_position[1] - 1

	if is_at_edge(my_map, my_position, direction):
		my_face = face(my_position)

		if direction == RIGHT:

			if my_face == "B":
				new_row = top_left["D"][0] + 49 - (row - top_left["B"][0])
				new_column = top_left["D"][1] + 49
				new_direction = LEFT

			elif my_face == "C":
				new_row = top_left["B"][0] + 49
				new_column = top_left["B"][1] + row - top_left["C"][0]
				new_direction = UP

			elif my_face == "D":
				new_row = top_left["B"][0] + 49 - (row - top_left["D"][0])
				new_column = top_left["B"][1] + 49
				new_direction = LEFT

			elif my_face == "F":
				new_row = top_left["D"][0] + 49
				new_column = top_left["D"][1] + (row - top_left["F"][0])
				new_direction = UP

			else:
				print("should not happen")


		if direction == LEFT:
			
			if my_face == "A":
				new_row = top_left["E"][0] + (49 - (row - top_left["A"][0]))
				new_column = top_left["E"][1]
				new_direction = RIGHT

			elif my_face == "C":
				new_row = top_left["E"][0]
				new_column = top_left["E"][1] + (row - top_left["C"][0])
				new_direction = DOWN

			elif my_face == "E":
				new_row = top_left["A"][0] + (49 - (row - top_left["E"][0]))
				new_column = top_left["A"][1]
				new_direction = RIGHT

			elif my_face == "F":
				new_row = top_left["A"][0]
				new_column = top_left["A"][1] + (row - top_left["F"][0])
				new_direction = DOWN

			else:
				print("should not happen")

		if direction == DOWN:
			
			if my_face == "F":
				new_row = top_left["B"][0]
				new_column = top_left["B"][1] + (column - top_left["F"][1])
				new_direction = DOWN

			elif my_face == "D":
				new_row = top_left["F"][0] + (column - top_left["D"][1])
				new_column = top_left["F"][1] + 49
				new_direction = LEFT

			elif my_face == "B":
				new_row = top_left["C"][0] + (column - top_left["B"][1])
				new_column = top_left["C"][1] + 49
				new_direction = LEFT

			else:
				print("should not happen")

		if direction == UP:
			
			if my_face == "E":
				new_row = top_left["C"][0] + (column - top_left["E"][1])
				new_column = top_left["C"][1]
				new_direction = RIGHT

			elif my_face == "A":
				new_row = top_left["F"][0] + (column - top_left["A"][1])
				new_column = top_left["F"][1]
				new_direction = RIGHT

			elif my_face == "B":
				new_row = top_left["F"][0] + 49
				new_column = top_left["F"][1] + (column - top_left["B"][1])
				new_direction = UP

			else:
				print("should not happen")

	else:
		new_row = row
		new_column = column

		new_row += (direction == UP) * -1 + (direction == DOWN) * 1
		new_column += (direction == LEFT) * -1 + (direction == RIGHT) * 1
		new_direction = my_direction

	return my_map[new_row][new_column] != "#", (new_row + 1, new_column + 1), new_direction

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
		can_move = True
		while number_pas > 0 and can_move:
			number_pas -= 1
			can_move, temp_position, temp_direction = move(my_map, my_position, my_direction)

			if can_move:
				my_position = temp_position
				my_direction = temp_direction


value_direction = {
	RIGHT : 0,
	DOWN : 1,
	LEFT : 2,
	UP : 3
}

print(1000 * my_position[0] + 4 * my_position[1] + value_direction[my_direction])

# print(my_map[top_left["A"][0]][top_left["A"][1]])
# print(my_map[top_left["B"][0]][top_left["B"][1]])
# print(my_map[top_left["C"][0]][top_left["C"][1]])
# print(my_map[top_left["D"][0]][top_left["D"][1]])
# print(my_map[top_left["E"][0]][top_left["E"][1]])
# print(my_map[top_left["F"][0]][top_left["F"][1]])
