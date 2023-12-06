with open('input') as f:
	data = list(map(lambda x: x.split('\n')[0], f.readlines()))

FACE_TOP = 0
FACE_BOTTOM = 1
FACE_X_PLUS = 2
FACE_X_MINUS = 3
FACE_Y_PLUS = 4
FACE_Y_MINUS = 5

class Cubes():

	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

		self.face_not_check = set()
		for face in range(6):
			self.face_not_check.add(face)

	def have_not_check(self, face):
		return face in self.face_not_check

	def check(self, face):
		self.face_not_check.remove(face)

cubes = {}

for ind, string in enumerate(data):
	x, y, z = map(int, string.split(','))

	cubes[(x, y, z)] = Cubes(x, y, z)

result = 0

for cube in cubes.values():

	x = cube.x
	y = cube.y
	z = cube.z

	for face_to_check in cube.face_not_check:

		if face_to_check == FACE_TOP:
			if (x, y, z + 1) in cubes:
				cubes[(x, y, z + 1)].check(FACE_BOTTOM)
			else:
				result += 1

		if face_to_check == FACE_BOTTOM:
			if (x, y, z - 1) in cubes:
				cubes[(x, y, z - 1)].check(FACE_TOP)
			else:
				result += 1

		if face_to_check == FACE_X_PLUS:
			if (x + 1, y, z) in cubes:
				cubes[(x + 1, y, z)].check(FACE_X_MINUS)
			else:
				result += 1

		if face_to_check == FACE_X_MINUS:
			if (x - 1, y, z) in cubes:
				cubes[(x - 1, y, z)].check(FACE_X_PLUS)
			else:
				result += 1

		if face_to_check == FACE_Y_PLUS:
			if (x, y + 1, z) in cubes:
				cubes[(x, y + 1, z)].check(FACE_Y_MINUS)
			else:
				result += 1

		if face_to_check == FACE_Y_MINUS:
			if (x, y - 1, z) in cubes:
				cubes[(x, y - 1, z)].check(FACE_Y_PLUS)
			else:
				result += 1

	cube.face_not_check = []

print(result)