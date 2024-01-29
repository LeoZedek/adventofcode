def neighbours(_map, y, x):

	result = set()

	for delta in ((1, 0), (-1, 0), (0, 1), (0, -1)):

		i = y + delta[0]
		j = x + delta[1]

		if 0 <= i and i < len(_map) and 0 <= j and j < len(_map[i]) and _map[i][j] != "#":
			result.add((i, j))

	return result

with open("input", "r") as file:
	data = file.readlines()

for i in range(len(data)):
	data[i] = data[i].strip()

for i in range(len(data)):
	for j in range(len(data[i])):

		if data[i][j] == "S":
			y_start = i
			x_start = j

infos = {}

distances = {
	(y_start, x_start): 0
}

queue = [(y_start, x_start)]
already_visited = set()
already_visited.add((y_start, x_start))

while len(queue) > 0:

	y, x = queue.pop(0)

	for neighbour in neighbours(data, y, x):

		if not(neighbour in already_visited):
			already_visited.add(neighbour)
			distances[neighbour] = distances[(y, x)] + 1
			queue.append(neighbour)

infos["middle"] = distances

configurations = [("top-left", (0, 0), 65), ("top", (0, 65), 131), ("top-right", (0, 130), 65), ("left", (65, 0), 131), ("right", (65, 130), 131), ("bottom-left", (130, 0), 65), ("bottom", (130, 65), 131), ("bottom-right", (130, 130), 65)]
configurations_big_sides = [("top-left-big", (0, 0), 131 + 65), ("top-right-big", (0, 130), 131 + 65), ("bottom-left-big", (130, 0), 131 + 65), ("bottom-right-big", (130, 130), 131 + 65)]

for config in configurations + configurations_big_sides:
	name, start_pos, max_dist = config

	y_start, x_start = start_pos

	distances = {
		(y_start, x_start): 0
	}

	queue = [(y_start, x_start)]
	already_visited = set()
	already_visited.add((y_start, x_start))

	while len(queue) > 0:

		y, x = queue.pop(0)

		for neighbour in neighbours(data, y, x):

			if not(neighbour in already_visited) and distances[(y, x)] + 1 < max_dist:
				already_visited.add(neighbour)
				distances[neighbour] = distances[(y, x)] + 1
				queue.append(neighbour)

	infos[name] = distances

spikes = ("top", "left", "right", "bottom")
sides = ("top-left", "top-right", "bottom-right", "bottom-left")
big_sides = ("top-left-big", "top-right-big", "bottom-right-big", "bottom-left-big")

# number tile : len(distances) = 14789

# (26501365 - 65) / 131 = 202300 radius
# ((202300 * 2  + 1) ** 2 - 1) / 2  = 81850984600 number of square (without the center)
# 4 spike
# 202300 length side
# 202299 length big sides

# print((26501365 - 65) / 131)
# print(((202300 * 2  + 1) ** 2 - 1) / 2)

print(81850984600 - 4 - 202299 * 4)
#  81850175404 Number of full square without the center

result = 0

even_square = 0
odd_square = 0

for i in range(202300 - 1):
	if i % 2 == 0:
		odd_square += 4 * i + 4
	else:
		even_square += 4 * i + 4

even_square += 1

for position, distance in infos["middle"].items():
	if distance % 2 == 1:
		result += even_square
	else:
		result += odd_square

for spike_name in spikes:

	for position, distance in infos[spike_name].items():
		if distance % 2 == 0:
			result += 1

for sides_name in sides:

	for position, distance in infos[sides_name].items():
		if distance % 2 == 0:
			result += 202300

for sides_name_big in big_sides:

	for position, distance in infos[sides_name_big].items():
		if distance % 2 == 1:
			result += 202299

print(result)