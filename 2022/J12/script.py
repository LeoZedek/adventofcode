import itertools

f = open('input')

data = list(map(lambda x : x.split('\n')[0], f.readlines()))

f.close()

n, p = (len(data), len(data[0]))

as_position = []

for i, j in itertools.product(range(n), range(p)):
	if data[i][j] == "S":
		start_pos = (i, j)
		as_position.append(start_pos)

	elif data[i][j] == "a":
		as_position.append((i, j))

	elif data[i][j] == "E":
		exit_pos = (i, j)

def neighbors(pos):
	i = pos[0]
	j = pos[1]

	result = []

	if i - 1 >= 0:
		result.append((i - 1, j))

	if i + 1 < n:
		result.append((i + 1, j))

	if j - 1 >= 0:
		result.append((i, j - 1))

	if j + 1 < p:
		result.append((i, j + 1))

	return result

def accessible(current_pos, neighbor):
	current_char = data[current_pos[0]][current_pos[1]]
	neighbor_char = data[neighbor[0]][neighbor[1]]

	if current_char == 'S':
		return ord('a') >= ord(neighbor_char) - 1

	elif neighbor_char == 'E':
		return ord(current_char) >= ord('z') - 1

	else:
		return ord(current_char) >= ord(neighbor_char) - 1

min_distance_for_a = {}

for a_position in as_position:
	start_pos = a_position

	queue = []

	queue.append(start_pos)

	visited_positions = set()
	visited_positions.add(start_pos)

	distance = {}
	distance[start_pos] = 0

	while len(queue) > 0 and not(exit_pos in visited_positions):
		current_pos = queue.pop(0)

		for neighbor in neighbors(current_pos):

			if not(neighbor in visited_positions) and accessible(current_pos, neighbor):

				queue.append(neighbor)
				visited_positions.add(neighbor)
				distance[neighbor] = distance[current_pos] + 1

	if (exit_pos in distance):

		min_distance_for_a[a_position] = distance[exit_pos]

print(min(min_distance_for_a.values()))