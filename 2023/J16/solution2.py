RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

STRAIGHT = 0
TURN_LEFT = 1
TURN_RIGHT = 2

DIRECTIONS = [RIGHT, DOWN, LEFT, UP]

directions_delta = {
	RIGHT : (0, 1),
	DOWN : (1, 0),
	LEFT : (0, -1),
	UP : (-1, 0)
}

name = {
	RIGHT: "right",
	LEFT : "left",
	DOWN : "down",
	UP : "up"
}

class Beam:
	def __init__(self, y, x, direction):
		self.y = y
		self.x = x
		self.direction = direction

	def __repr__(self):
		return "y = " + str(self.y) + "; x = " + str(self.x) + "; direction = " + name[self.direction]

def plus_90_degre(direction):
	return DIRECTIONS[(DIRECTIONS.index(direction) - 1) % len(DIRECTIONS)]

def minus_90_degre(direction):
	return DIRECTIONS[(DIRECTIONS.index(direction) + 1) % len(DIRECTIONS)]

def go_beam(old_beam, way):
	if way == STRAIGHT:

		new_direction = old_beam.direction

	elif way == TURN_LEFT:

		new_direction = plus_90_degre(old_beam.direction)

	else:

		new_direction = minus_90_degre(old_beam.direction)

	delta = directions_delta[new_direction]

	new_y = old_beam.y + delta[0]
	new_x = old_beam.x + delta[1]

	return Beam(new_y, new_x, new_direction)

def in_map(_map, beam):
	return beam.y >= 0 and beam.y < len(_map) and beam.x >= 0 and beam.x < len(_map[0])

def calcul_score(initial_beam):
	beams = [initial_beam]

	energized_tiles = {}

	already_done = set()

	while len(beams) > 0:

		new_beams = []

		for beam in beams:

			y = beam.y
			x = beam.x
			energized_tiles[(y, x)] = True

			already_done.add((y, x, beam.direction))

			if _map[y][x] == ".":

				new_beams.append(go_beam(beam, STRAIGHT))

			elif _map[y][x] == "/":

				if beam.direction == LEFT or beam.direction == RIGHT:
					new_beams.append(go_beam(beam, TURN_LEFT))

				else:
					new_beams.append(go_beam(beam, TURN_RIGHT))

			elif _map[y][x] == "\\":

				if beam.direction == LEFT or beam.direction == RIGHT:
					new_beams.append(go_beam(beam, TURN_RIGHT))

				else:
					new_beams.append(go_beam(beam, TURN_LEFT))

			elif _map[y][x] == "-":

				if beam.direction == LEFT or beam.direction == RIGHT:
					new_beams.append(go_beam(beam, STRAIGHT))

				else:

					new_beams.append(go_beam(beam, TURN_LEFT))
					new_beams.append(go_beam(beam, TURN_RIGHT))

			elif _map[y][x] == "|":

				if beam.direction == UP or beam.direction == DOWN:
					new_beams.append(go_beam(beam, STRAIGHT))

				else:

					new_beams.append(go_beam(beam, TURN_LEFT))
					new_beams.append(go_beam(beam, TURN_RIGHT))

		beams = []

		for new_beam in new_beams:

			if in_map(_map, new_beam) and not((new_beam.y, new_beam.x, new_beam.direction) in already_done):
				beams.append(new_beam)

	return len(energized_tiles)

with open("input", "r") as file:

	data = file.readlines()

for i in range(len(data)):
	data[i] = data[i].strip()

_map = data

max_score = 0

for i in range(len(_map)):

	beam = Beam(i, 0, RIGHT)
	score = calcul_score(beam)

	if score > max_score:
		max_score = score

	beam = Beam(i, len(_map[0]) - 1, LEFT)
	score = calcul_score(beam)

	if score > max_score:
		max_score = score

for j in range(len(_map[0])):

	beam = Beam(0, j, DOWN)
	score = calcul_score(beam)

	if score > max_score:
		max_score = score

	beam = Beam(len(_map) - 1, j, UP)
	score = calcul_score(beam)

	if score > max_score:
		max_score = score

print(max_score)