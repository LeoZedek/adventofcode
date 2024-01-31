X = 0
Y = 1
Z = 2

AXIS = {X, Y, Z}

class Brick:

	def __init__(self, end1, end2):

		self.end1 = end1
		self.end2 = end2
		self.z_length = end2[Z] - end1[Z] + 1

	def __hash__(self):
		return hash(self.end1 + self.end2)

	def __eq__(self, other):
		return hash(self) == hash(other)

	def is_inside(self, coord):
		for axe in AXIS:
			if not(self.end1[axe] <= coord[axe] and coord[axe] <= self.end2[axe]):
				return False

		return True

	def upper_brick(self):
		if self.end1[Z] != self.end2[Z]:
			return {(self.end2[X], self.end2[Y], self.end2[Z] + 1)}

		upper_bricks = set()

		for i in range(self.end1[X], self.end2[X] + 1):
			for j in range(self.end1[Y], self.end2[Y] + 1):
				upper_bricks.add((i, j, self.end2[Z] + 1))

		return upper_bricks

	def is_on_ground(self):
		return self.end1[Z] == 1

	def is_bricks_under(self, cubes):
		for i in range(self.end1[X], self.end2[X] + 1):
			for j in range(self.end1[Y], self.end2[Y] + 1):

				if (i, j, self.end1[Z] - 1) in cubes:
					return True
					# for brick in bricks:
					# 	if brick.is_inside((i, j, self.end1[Z] - 1)):
					# 		return True

		return False

	def fall_one(self):
		end1 = (self.end1[X], self.end1[Y], self.end1[Z] - 1)
		end2 = (self.end2[X], self.end2[Y], self.end2[Z] - 1)

		return Brick(end1, end2)

	def fall(self, cubes_on_ground):
		result = self

		while not(result.is_bricks_under(cubes_on_ground) or result.is_on_ground()):
			result = result.fall_one()

		return result

	def __repr__(self):
		return str(self.end1) + "," + str(self.end2)

def add_cubes(cubes, brick):
	for i in range(brick.end1[X], brick.end2[X] + 1):
		for j in range(brick.end1[Y], brick.end2[Y] + 1):
			for k in range(brick.end1[Z], brick.end2[Z] + 1):
				cubes.add((i, j, k))

with open("input", "r") as file:

	data = file.readlines()

snapshot_bricks = []

for i in range(len(data)):

	end_brick_1, end_brick_2 = map(lambda x : tuple(map(int, x.split(","))), data[i].strip().split("~"))

	snapshot_bricks.append(Brick(end_brick_1, end_brick_2))

snapshot_bricks.sort(key = lambda x : x.end1[Z])

fallen_bricks = set()
all_cubes = set()

suporte = {}
is_supported_by = {}

for i in range(len(snapshot_bricks)):
	falling_brick = snapshot_bricks[i]

	fallen_brick = falling_brick.fall(all_cubes)

	fallen_bricks.add(fallen_brick)
	add_cubes(all_cubes, fallen_brick)
	suporte[fallen_brick] = set()
	is_supported_by[fallen_brick] = set()

for brick in fallen_bricks:
	for upper_cube in brick.upper_brick():
		for brick_2 in fallen_bricks:
			if brick_2.is_inside(upper_cube):
				suporte[brick].add(brick_2)
				is_supported_by[brick_2].add(brick)

bricks_to_fall = set()

def is_all_in(child, parent):
	for elt in child:
		if not(elt in parent):
			return False
	return True

def number_brick_to_fall(brick, disintegrated_bricks):
	result = 0

	supported_bricks = suporte[brick]

	chain_bricks = set()
	disintegrated_bricks.add(brick)

	for supported_brick in supported_bricks:
		if is_all_in(is_supported_by[supported_brick], disintegrated_bricks):
			chain_bricks.add(supported_brick)
			result += 1

	
	for chain_brick in chain_bricks:
		if not(chain_brick in disintegrated_bricks):
			result += number_brick_to_fall(chain_brick, disintegrated_bricks)

	return result

result = 0

for brick in fallen_bricks:

	result += number_brick_to_fall(brick, {brick})

print(result)