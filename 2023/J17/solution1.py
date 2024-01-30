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
		result.add(Crucible(0, 1, RIGHT, 1))

		result.add(Crucible(1, 0, DOWN, 1))

	else:

		for direction, delta in deltas.items():

			if not(direction == opposite_direction[crucible.direction]) and not(crucible.straight_counter == 3 and direction == crucible.direction):

				if direction == crucible.direction:
			  		new_counter = crucible.straight_counter + 1
				else:
			  		new_counter = 1

				if is_in_bound(data, crucible.y + delta[0], crucible.x + delta[1]):
					result.add(Crucible(crucible.y + delta[0], crucible.x + delta[1], direction, new_counter))

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

		new_heat = heat_loss[current_crucible] + data[neigbour.y][neigbour.x]

		if not(neigbour in heat_loss) or new_heat < heat_loss[neigbour]:
			heat_loss[neigbour] = new_heat
			Q.put((new_heat, neigbour))
