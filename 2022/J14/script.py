with open('input') as f:
	data = list(map(lambda x : x.split('\n')[0], f.readlines()))

ROCK = 0
SAND = 1
AIR = 2

sand_pouring = (500, 0)

obstacles = {}

for ind, string in enumerate(data):

	string_list = string.split(' -> ')

	for i in range(len(string_list) - 1):
		x1, y1 = list(map(int, string_list[i].split(',')))
		x2, y2 = list(map(int, string_list[i + 1].split(',')))

		if x1 == x2:
			for y in range(min(y1, y2), max(y2, y1) + 1):
				obstacles[(x1, y)] = ROCK

		else:
			for x in range(min(x1, x2), max(x1, x2) + 1):
				obstacles[(x, y1)] = ROCK

#minY = min(obstacles, key = lambda x : x[1])[1]
maxY = max(obstacles, key = lambda x : x[1])[1]

sand_rest = False
sand_void = False
number_sand = 0

while not(sand_void):

	sand_pos = sand_pouring
	sand_rest = False

	while not(sand_rest) and not(sand_void):

		if (sand_pos[1] >= maxY):
			sand_void = True

		elif not((sand_pos[0], sand_pos[1] + 1) in obstacles):
			sand_pos = (sand_pos[0], sand_pos[1] + 1)

		elif not((sand_pos[0] - 1, sand_pos[1] + 1) in obstacles):
			sand_pos = (sand_pos[0] - 1, sand_pos[1] + 1)

		elif not((sand_pos[0] + 1, sand_pos[1] + 1) in obstacles):
			sand_pos = (sand_pos[0] + 1, sand_pos[1] + 1)

		else:
			obstacles[sand_pos] = SAND
			number_sand += 1
			sand_rest = True

print(number_sand)