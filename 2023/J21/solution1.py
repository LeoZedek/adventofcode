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

result = 0

for position, distance in distances.items():
	if distance <= 64 and distance % 2 == 0:
		result += 1

print(result)
