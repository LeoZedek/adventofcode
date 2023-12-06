with open('input') as f:
	data = list(map(lambda x: x.split('\n')[0], f.readlines()))

cubes = set()

for ind, string in enumerate(data):
	x, y, z = map(int, string.split(','))

	cubes.add((x, y, z))

min_x = min(cubes, key = lambda x : x[0])[0] - 1
max_x = max(cubes, key = lambda x : x[0])[0] + 1
min_y = min(cubes, key = lambda x : x[1])[1] - 1
max_y = max(cubes, key = lambda x : x[1])[1] + 1
min_z = min(cubes, key = lambda x : x[2])[2] - 1
max_z = max(cubes, key = lambda x : x[2])[2] + 1

def neighbours(location):

	x, y, z = location
	result = set()

	if x - 1 >= min_x:
		result.add((x - 1, y, z))

	if x + 1 <= max_x:
		result.add((x + 1, y, z))

	if y - 1 >= min_y:
		result.add((x, y - 1, z))

	if y + 1 <= max_y:
		result.add((x, y + 1, z))

	if z - 1 >= min_z:
		result.add((x, y, z - 1))

	if z + 1 <= max_z:
		result.add((x, y, z + 1))

	return result

result = 0

begin = (min_x, min_y, min_z)
already_visited = set()

queue = []
queue.append(begin)
already_visited.add(begin)

while len(queue) > 0:

	current_location = queue.pop(0)

	for neighbour in neighbours(current_location):

		if not(neighbour in already_visited):

			if neighbour in cubes:
				result += 1

			else:
				queue.append(neighbour)
				already_visited.add(neighbour)

print(result)