import re
from collections import defaultdict

ROWS = 103
COLUMNS = 101

AROUND = [(1, 1), (1, -1), (1, 0)]

class Robot:
	def __init__(self, p_row, p_col, v_row, v_col):
		self.p_row = p_row
		self.p_col = p_col
		self.v_row = v_row
		self.v_col = v_col

	def move(self, seconds):
		self.p_row = (self.p_row + seconds * self.v_row) % ROWS
		self.p_col = (self.p_col + seconds * self.v_col) % COLUMNS

def add_border(matrix, char, width):
	for i in range(len(matrix)):
		matrix[i] = char * width + matrix[i] + char * width

	matrix.append(char * len(matrix[0]))
	matrix.insert(0, char * len(matrix[0]))


def create_map(robots):
	robots_position = defaultdict(int)

	for robot in robots:
		robots_position[(robot.p_row, robot.p_col)] += 1

	_map = []

	for i in range(ROWS):
		_map.append([])

		for j in range(COLUMNS):
			_map[i].append(str(robots_position[(i, j)]) if robots_position[(i, j)] != 0 else '.')

		_map[i] = ''.join(_map[i])

	return _map

def is_most_robots_close(robots, _map, percentage):
	temp_map = _map.copy()
	add_border(temp_map, '.', 1)

	robots_close = 0
	for robot in robots:
		close = False

		for di in range(-1, 2):
			for dj in range(-1, 2):
				if di == 0 and dj == 0:
					if int(temp_map[robot.p_row + 1][robot.p_col + 1]) > 1:
						close = True
				elif temp_map[robot.p_row + 1+ di][robot.p_col + 1 + dj] != '.':
					close = True
		robots_close += close

	return robots_close / len(robots) >= percentage


with open('input') as file:
	data = file.read().splitlines()

robots = set()

for line in data:
	pos = re.search(r'p=\d+,\d+', line).group()[2:]
	p_col, p_row = list(map(int, pos.split(',')))
	velocity = re.search(r'v=-?\d+,-?\d+', line).group()[2:]
	v_col, v_row = list(map(int, velocity.split(',')))

	robots.add(Robot(p_row, p_col, v_row, v_col))

quadrants = defaultdict(int)
with open('output', 'w') as file:

	for i in range(10000):

		for robot in robots:
			robot.move(1)

		_map = create_map(robots)

		if is_most_robots_close(robots, _map, 0.7):
			print(i + 1)

			for row in _map:
				file.write(row)
				file.write('\n')
			file.write('\n')