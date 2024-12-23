import re
from collections import defaultdict

ROWS = 103
COLUMNS = 101

class Robot:
	def __init__(self, p_row, p_col, v_row, v_col):
		self.p_row = p_row
		self.p_col = p_col
		self.v_row = v_row
		self.v_col = v_col

	def move(self, seconds):
		self.p_row = (self.p_row + seconds * self.v_row) % ROWS
		self.p_col = (self.p_col + seconds * self.v_col) % COLUMNS

def create_map(robots):
	robots_position = defaultdict(int)

	for robot in robots:
		robots_position[(robot.p_row, robot.p_col)] += 1

	_map = []

	for i in range(ROWS):
		_map.append([])

		for j in range(COLUMNS):
			_map.append(str(robots_positions[(i, j)]) if robots_positions[(i, j)] != 0 else '.')

	return _map

with open('input') as file:
	data = file.read().splitlines()

robots = set()

for line in data:
	pos = re.search('p=\d+,\d+', line).group()[2:]
	p_col, p_row = list(map(int, pos.split(',')))
	velocity = re.search('v=-?\d+,-?\d+', line).group()[2:]
	v_col, v_row = list(map(int, velocity.split(',')))

	robots.add(Robot(p_row, p_col, v_row, v_col))

quadrants = defaultdict(int)

for robot in robots:
	robot.move(1)


with open('output', 'w') as file:
	first_map = create_map(robots)