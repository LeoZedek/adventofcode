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
	robot.move(100)

	if robot.p_row < ROWS // 2 and robot.p_col < COLUMNS // 2:
		quadrants['left-top'] += 1
	elif robot.p_row > ROWS // 2 and robot.p_col < COLUMNS // 2:
		quadrants['right-top'] += 1
	elif robot.p_row < ROWS // 2 and robot.p_col > COLUMNS // 2:
		quadrants['left-bottom'] += 1
	elif robot.p_row > ROWS // 2 and robot.p_col > COLUMNS // 2:
		quadrants['right-bottom'] += 1

r = 1

for value in quadrants.values():
	r *= value

print(r)