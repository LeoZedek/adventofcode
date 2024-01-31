class Coord:
	def __init__(self, y, x):
		self.y = y
		self.x = x

	def __add__(self, coord2):
		return Coord(self.y + coord2.y, self.x + coord2.x)

	@property
	def tuple(self):
		return (self.y, self.x)

def is_inside_trench(trench, max_x, pos):
	x = pos[1]
	y = pos[0]

	new_x = x + 1

	border_cross = 0

	while new_x <= max_x:
		if (y, new_x) in trench:

			border = trench[(y, new_x)]

			if border == '|':
				border_cross += 1

			elif border == 'L' or border == 'F':
				first_border = border

				while trench[(y, new_x)] != 'J' and trench[(y, new_x)] != '7':
					new_x += 1

				if (first_border == 'L' and trench[(y, new_x)] == '7') or (first_border == 'F' and trench[(y, new_x)] == 'J'):
					border_cross += 1

		new_x += 1

	if border_cross % 2 == 0:
		return False
	else:
		return True


def get_symbole(direction1, direction2):

	directions = (direction1, direction2)

	if ("R" in directions and "L" in directions) or (direction1 == direction2 and (direction1 == "L" or direction1 == "R")):
		return "-"

	if ("U" in directions and "D" in directions) or (direction1 == direction2 and (direction1 == "U" or direction1 == "D")):
		return "|"

	if (direction1 == "R" and direction2 == "D") or (direction1 == "U" and direction2 == "L"):
		return "7"

	if (direction1 == "D" and direction2 == "R") or (direction1 == "L" and direction2 == "U"):
		return "L"

	if (direction1 == "D" and direction2 == "L") or (direction1 == "R" and direction2 == "U"):
		return "J"

	if (direction1 == "U" and direction2 == "R") or (direction1 == "L" and direction2 == "D"):
		return "F"

	print("should not happen")
	return None

deltas = {
	"R": Coord(0, 1),
	"L": Coord(0, -1),
	"U": Coord(-1, 0),
	"D": Coord(1, 0)
}

with open("input", "r") as file:
	data = file.readlines()

trench = {}
paints = {}

trench_order = []
direction_order = []

current_coord = Coord(0, 0)

min_x = 0
max_x = 0
min_y = 0
max_y = 0

for count, line in enumerate(data):
	line = line.strip()

	direction, n_step, color = line.split()

	if count == 0:
		first_direction = direction
		previous_direction = None

	n_step = int(n_step)
	color = color[2: -1]

	for i in range(n_step):
		current_coord += deltas[direction]

		paints[current_coord.tuple] = color
		trench_order.append(current_coord.tuple)
		direction_order.append(direction)
		
		min_y = min(current_coord.y, min_y)
		max_y = max(current_coord.y, max_y)
		min_x = min(current_coord.x, min_x)
		max_x = max(current_coord.x, max_x)

for i in range(len(trench_order)):
	coord = trench_order[i]

	trench[coord] = get_symbole(direction_order[i], direction_order[(i+1) % len(direction_order)])

interior = []

for i in range(min_y, max_y + 1):
	for j in range(min_x, max_x + 1):
		if not((i, j) in trench) and is_inside_trench(trench, max_x, (i, j)):
			interior.append((i, j))

print(len(interior) + len(trench))

#print(interior)