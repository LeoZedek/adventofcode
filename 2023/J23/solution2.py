import sys

deltas = {
	(1, 0),
	(-1, 0),
	(0, 1),
	(0, -1)
}

def is_in_bound(x, y):
	return 0 <= x and x < len(data[0]) and 0 <= y and y < len(data)

def is_intersection(pos):
	number_ways = 0

	for delta in deltas:
		new_y, new_x = tuple((pos[i] + delta[i] for i in range(len(delta))))

		if is_in_bound(new_x, new_y) and data[new_y][new_x] != "#":
			number_ways += 1

	return number_ways > 2

def neigbour_data(pos):
	result = set()

	for delta in deltas:
		y, x = tuple((pos[i] + delta[i] for i in range(len(delta))))

		if is_in_bound(x, y) and data[y][x] != "#":
			result.add((y, x))

	return result

with open("input", "r") as file:
	data = file.readlines()

data = list(map(lambda x: x.strip(), data))

for j in range(len(data[0])):
	if data[0][j] == ".":
		start = (0, j)

	if data[-1][j] == ".":
		end = (len(data) - 1, j)

intersections = set()

neigbours = {}
distances = {}

for i in range(len(data)):
	for j in range(len(data[i])):
		if data[i][j] != "#" and is_intersection((i, j)):

			intersections.add((i, j))
			neigbours[(i, j)] = set()

for intersection in intersections:

	distance_temp = {intersection : 0}
	queue = [intersection]
	already_visited = {intersection}

	while len(queue) > 0:

		pos = queue.pop(0)

		for neigbour in neigbour_data(pos):
			if not(neigbour in already_visited):
				if neigbour in intersections:
					neigbours[intersection].add(neigbour)
					neigbours[neigbour].add(intersection)
					distances[(intersection, neigbour)] = distance_temp[pos] + 1
					distances[(neigbour, intersection)] = distance_temp[pos] + 1
				else:
					distance_temp[neigbour] = distance_temp[pos] + 1
					already_visited.add(neigbour)
					queue.append(neigbour)

distance_temp = {start : 0}
queue = [start]
already_visited = {start}

while len(queue) > 0:

	pos = queue.pop(0)

	for neigbour in neigbour_data(pos):
		if not(neigbour in already_visited):
			if neigbour in intersections:
				start_intersection = neigbour
				start_distance = distance_temp[pos] + 1
			else:
				distance_temp[neigbour] = distance_temp[pos] + 1
				already_visited.add(neigbour)
				queue.append(neigbour)

distance_temp = {end : 0}
queue = [end]
already_visited = {end}

while len(queue) > 0:

	pos = queue.pop(0)

	for neigbour in neigbour_data(pos):
		if not(neigbour in already_visited):
			if neigbour in intersections:
				end_intersection = neigbour
				end_distance = distance_temp[pos] + 1
			else:
				distance_temp[neigbour] = distance_temp[pos] + 1
				already_visited.add(neigbour)
				queue.append(neigbour)

def get_max_distance(current_intersection, already_visited):

	if current_intersection == end_intersection:
		return 0

	already_visited.add(current_intersection)

	max_distance = 0

	for neigbour_intersection in neigbours[current_intersection]:
		if not(neigbour_intersection in already_visited):
			distance_temp = distances[(current_intersection, neigbour_intersection)] + get_max_distance(neigbour_intersection, already_visited.copy())
			if distance_temp > max_distance:
				max_distance = distance_temp

	return max_distance

print(get_max_distance(start_intersection, set()) + start_distance + end_distance)
