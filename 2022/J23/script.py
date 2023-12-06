with open('input') as f:
	data = list(map(lambda x : x.split('\n')[0], f.readlines()))

NORTH = 0
SOUTH = 1
WEST = 2
EAST = 3

check_direction_order = [NORTH, SOUTH, WEST, EAST]

class Elve():

	def __init__(self, x_pos, y_pos):
		self.x = x_pos
		self.y = y_pos

		self.proposition_moving	= (x_pos, y_pos)

	def is_alone(self, elves):

		for i in range(self.x - 1, self.x + 2):
			for j in range(self.y - 1, self.y + 2):
				if not(i == self.x and j ==  self.y) and (i, j) in elves:
					return False

		return True

	def propose_moving(self, elves):

		x, y = self.x, self.y

		for ind, direction in enumerate(check_direction_order):

			if direction == NORTH:

				if not((x - 1, y) in elves) and not((x - 1, y - 1) in elves) and not((x - 1, y + 1) in elves):
					self.proposition_moving = (x - 1, y)
					return True, self.proposition_moving

			elif direction == SOUTH:

				if not((x + 1, y) in elves) and not((x + 1, y - 1) in elves) and not((x + 1, y + 1) in elves):
					self.proposition_moving = (x + 1, y)
					return True, self.proposition_moving

			elif direction == WEST:

				if not((x, y - 1) in elves) and not((x + 1, y - 1) in elves) and not((x - 1, y - 1) in elves):
					
					self.proposition_moving = (x, y - 1)
					return True, self.proposition_moving

			elif direction == EAST:

				if not((x, y + 1) in elves) and not((x + 1, y + 1) in elves) and not((x - 1, y + 1) in elves):
					
					self.proposition_moving = (x, y + 1)
					return True, self.proposition_moving

			else:
				print("should not happend")

		self.proposition_moving = (x, y)
		return False, self.proposition_moving

	def reset_proposition_move(self):
		self.proposition_moving = (self.x, self.y)

elves = {}

for i in range(len(data)):
	for j in range(len(data[i])):
		if data[i][j] == "#":
			elves[(i, j)] = Elve(i, j)

elve_move = True
number_round = 0
## Where is the love

while elve_move:

	elve_move = False

	proposed_destinations = {}

	## Check propposition moving

	for elve in elves.values():

		if elve.is_alone(elves):
			elve.reset_proposition_move()
			proposed_destinations[elve.proposition_moving] = 1

		else:
			propose, proposed_move = elve.propose_moving(elves)

			if not(proposed_move in proposed_destinations):
				proposed_destinations[proposed_move] = 1
			else:
				proposed_destinations[proposed_move] += 1

	## Move the elves

	for elve in elves.copy().values():

		proposed_move = elve.proposition_moving

		if proposed_destinations[proposed_move] == 1 and proposed_move != (elve.x, elve.y):
			elve_move = True
			del elves[(elve.x, elve.y)]

			elve.x = proposed_move[0]
			elve.y = proposed_move[1]

			elves[(elve.x, elve.y)] = elve

		elve.reset_proposition_move()

	## Change direction order

	check_direction_order.append(check_direction_order.pop(0))
	number_round += 1

# min_x = min(elves.values(), key = lambda x : x.x).x
# max_x = max(elves.values(), key = lambda x : x.x).x
# min_y = min(elves.values(), key = lambda x : x.y).y
# max_y = max(elves.values(), key = lambda x : x.y).y

# print((max_x - min_x + 1) * (max_y - min_y + 1) - len(elves))

print(number_round)