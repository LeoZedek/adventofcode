import math

from queue import PriorityQueue

RIGHT = 0
LEFT = 1
UP = 2
DOWN = 3

deltas = {
	RIGHT: (0, 1),
	LEFT: (0, -1),
	UP: (-1, 0),
	DOWN: (1, 0)
}

opposite_direction = {
	RIGHT: LEFT,
	LEFT: RIGHT,
	UP: DOWN,
	DOWN: UP
}

directions = {RIGHT, LEFT, DOWN, UP}

class Crucible:

	def __init__(self, y, x, direction, straight_counter):
		self.y = y
		self.x = x
		self.direction = direction
		self.straight_counter = straight_counter

	@property
	def coord(self):
		return (self.y, self.x)

	def __hash__(self):
		return hash((self.y, self.x, self.direction, self.straight_counter))

	def __eq__(self, another):
		return hash(self) == hash(another)

	# def __repr__(self):
	# 	return "y : " + str(self.y) + "; x : " + str(self.x) + "; direction: " + str(self.direction) + "; count : " + str(self.straight_counter)

	def __repr__(self):
		return f"({str(self.coord)}, {self.direction}, {self.straight_counter})"

	def __lt__(self, other):
		return True

def is_in_bound(_map, y, x):
	return 0 <= y and y < len(_map) and 0 <= x and x < len(_map[0])

def get_neigbour(crucible):

	result = set()

	if crucible.straight_counter == 0:
		result.add(Crucible(0, 4, RIGHT, 4))

		result.add(Crucible(4, 0, DOWN, 4))

	else:

		for direction, delta in deltas.items():

			if not(direction == opposite_direction[crucible.direction]) and not(crucible.straight_counter == 10 and direction == crucible.direction):

				if direction == crucible.direction:
			  		new_counter = crucible.straight_counter + 1
			  		dx = delta[1]
			  		dy = delta[0]

				else:
			  		new_counter = 4
			  		dy = delta[0] * 4
			  		dx = delta[1] * 4

				if is_in_bound(data, crucible.y + dy, crucible.x + dx):
					result.add(Crucible(crucible.y + dy, crucible.x + dx, direction, new_counter))

	return result

with open("input", "r") as file:

	data = file.readlines()

for i in range(len(data)):
	data[i] = list(map(int, list(data[i].strip())))

end_point = (len(data) - 1, len(data[0]) - 1)

Q = PriorityQueue()
start = Crucible(0, 0, None, 0)

Q.put((0, start))

heat_loss = {
	start : 0
}

while not(Q.empty()):
	current_crucible = Q.get()[1]

	if current_crucible.coord == end_point:
		print(heat_loss[current_crucible])
		break

	for neigbour in get_neigbour(current_crucible):

		sum_heat_parkour = 0

		if neigbour.x == current_crucible.x:
			if neigbour.y > current_crucible.y:
				for i in range(current_crucible.y + 1, neigbour.y + 1):
					sum_heat_parkour += data[i][neigbour.x]

			else:
				for i in range(current_crucible.y - 1, neigbour.y - 1, -1):
					sum_heat_parkour += data[i][neigbour.x]

		else:
			if neigbour.x > current_crucible.x:
				for j in range(current_crucible.x + 1, neigbour.x + 1):
					sum_heat_parkour += data[neigbour.y][j]

			else:
				for j in range(current_crucible.x - 1, neigbour.x - 1, -1):
					sum_heat_parkour += data[neigbour.y][j]

		new_heat = heat_loss[current_crucible] + sum_heat_parkour

		if not(neigbour in heat_loss) or new_heat < heat_loss[neigbour]:
			heat_loss[neigbour] = new_heat
			Q.put((new_heat, neigbour))
