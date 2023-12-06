from time import time

time1 = time()

with open("input") as f:
	data = list(map(lambda x : x.split('\n')[0], f.readlines()))

winds = {'v', '^', '>', '<'}

height = len(data)
width = len(data[0])

begin_position = (0, 1)
exit_position = (height - 1, width - 2)

my_map = {}

for i in range(height):
	for j in range(width):

		if data[i][j] in winds:

			if not((i, j) in my_map):
				my_map[(i, j)] = {data[i][j]}

			else:
				my_map[(i, j)].add(data[i][j])

def add_to_dict(my_map, i, j, wind):
	if (i, j) in my_map:
		my_map[(i, j)].add(wind)
	else:
		my_map[(i, j)] = {wind}

def update(my_map):

	result = {}

	for coord, value in my_map.items():
		i, j = coord

		for wind in value:

			if wind == '^':
				if i - 1 >= 1:
					add_to_dict(result, i - 1, j, wind)

				else:
					add_to_dict(result, height - 2, j, wind)

			elif wind == 'v':

				if i + 1 < height - 1:
					add_to_dict(result, i + 1, j, wind)

				else:
					add_to_dict(result, 1, j, wind)

			elif wind == '<':

				if j - 1 >= 1:
					add_to_dict(result, i, j - 1, wind)

				else:
					add_to_dict(result, i, width - 2, wind)

			elif wind == '>':

				if j + 1 < width - 1:
					add_to_dict(result, i, j + 1, wind)

				else:
					add_to_dict(result, i, 1, wind)

	return result

def distance_manhatan(pos1, pos2):
	return abs(pos1[0] - pos2[0]) + abs(pos2[1] - pos1[1])

def is_valide(my_map, position):
	if position == (0, 1) or position == exit_position:
		return True

	else:
		if position[0] == 0 or position[0] == height - 1 or position[1] == 0 or position[1] == width - 1 or position in my_map:
			return False
		else:
			return True

def voisins(position, index):
	if index == seuil - 1:
		new_index = 0
	else:
		new_index = index + 1

	row, column = position

	voisins_possible = [(row, column), (row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1)]

	result = set()

	for voisin in voisins_possible:
		if is_valide(configuration_maps[new_index], voisin):
			result.add(voisin)

	return result

configuration_maps = {0 : my_map}

seuil = (height - 2) * (width - 2)

temp_map = my_map
for i in range(1, seuil):
	temp_map = update(temp_map)
	configuration_maps[i] = temp_map

print("Config maps finished")

def get_shorter_ways_BFS(begin, end, index_begin):
	distance = {}

	configuration_marque = set()

	queue = [(begin, index_begin)]

	distance[(begin, index_begin)] = 0

	configuration_marque.add((begin, index_begin))

	while len(queue) > 0:

		position, index = queue.pop(0)

		if index == seuil - 1:
			new_index = 0
		else:
			new_index = index + 1 

		for voisin in voisins(position, index):
			if not((voisin, new_index) in configuration_marque):
				distance[(voisin, new_index)] = distance[(position, index)] + 1

				queue.append((voisin, new_index))

				configuration_marque.add((voisin, new_index))

				if voisin == end:
					return distance[(end, new_index)], index

result = 0

minutes, index = get_shorter_ways_BFS(begin_position, exit_position, 0)

print(minutes)
result += minutes

minutes, index = get_shorter_ways_BFS(exit_position, begin_position, index)

print(minutes)
result += minutes

minutes, index = get_shorter_ways_BFS(begin_position, exit_position, index)

print(minutes)
result += minutes

print(result - 2)

time2 = time()

print("temps : " + str(time2 - time1))