from queue import PriorityQueue
from collections import defaultdict

RIGHT = '>'
UP = '^'
LEFT = '<'
DOWN = 'v'

POSITIONS = {
	'0': (4, 2),
	'A': (4, 3),
	'1': (3, 1),
	'2': (3, 2),
	'3': (3, 3),
	'4': (2, 1),
	'5': (2, 2),
	'6': (2, 3),
	'7': (1, 1),
	'8': (1, 2),
	'9': (1, 3),
	'^': (1, 2),
	'<': (2, 1),
	'v': (2, 2),
	'>': (2, 3)
}

A_directional_pad_pos = (1, 3)

DELTAS = {
	RIGHT: (0, 1),
	UP: (-1, 0),
	DOWN: (1, 0),
	LEFT: (0, -1),
	'A': (0, 0)
}

DEPTH = 25

def modify_tuple(node, new_pos, index):
	node_as_list = list(node)
	node_as_list[index] = new_pos
	return tuple(node_as_list)

def is_on_A(current_node, index):
	row, col = current_node[index]
	return directional_pad[row][col] == 'A'

def get_neigbours(current_node, numerical = False):
	position = current_node[0]
	neigbours = set()

	# <, >, v, ^ actions
	for action, delta in DELTAS.items():
		new_row, new_col = position[0] + delta[0], position[1] + delta[1]

		if numerical:
			_map = numeric_pad
		else:
			_map = directional_pad

		if _map[new_row][new_col] != '.':
			neigbours.add(((new_row, new_col), action))

	return neigbours

def distance_numerical(current_node, neigbour, memo):
	return distance_between(current_node[1], neigbour[1], DEPTH, memo)

def distance_between(char1, char2, depth, memo):
	key = (char1, char2, depth)
	if key in memo:
		return memo[key]

	if char1 == 'A':
		start = (A_directional_pad_pos, 'A')
	else:
		start = (POSITIONS[char1], 'A')
	if char2 == 'A':
		end = (A_directional_pad_pos, 'A')
	else:
		end = (POSITIONS[char2], 'A')

	if char1 == char2:
		return 1

	if depth == 1:
		memo[key] = abs(start[0][0] - end[0][0]) + abs(start[0][1] - end[0][1]) + 1
		return memo[key]

	Q = PriorityQueue()

	Q.put((0, start))

	distance = {
		start : 0
	}
	while not(Q.empty()):
		current_node = Q.get()[1]

		for neigbour in get_neigbours(current_node, numerical = False): ## get_neigbour to define

			new_distance = distance[current_node] + distance_between(current_node[1], neigbour[1], depth - 1, memo)

			if not(neigbour in distance) or new_distance < distance[neigbour]:

				distance[neigbour] = new_distance
				Q.put((new_distance, neigbour))

	memo[key] = distance[end]
	return memo[key]


def add_border(matrix, char, width):
	for i in range(len(matrix)):
		matrix[i] = char * width + matrix[i] + char * width

	matrix.append(char * len(matrix[0]))
	matrix.insert(0, char * len(matrix[0]))

def get_len_shortest_path_numerical(char1, char2, memo):
	key = (char1, char2)
	if key in memo:
		return memo[key]

	start = (POSITIONS[char1], 'A')
	end = (POSITIONS[char2], 'A')

	Q = PriorityQueue()

	Q.put((0, start))

	distance = {
		start : 0
	}
	while not(Q.empty()):
		current_node = Q.get()[1]

		for neigbour in get_neigbours(current_node, numerical = True): ## get_neigbour to define

			new_distance = distance[current_node] + distance_numerical(current_node, neigbour, memo)

			if not(neigbour in distance) or new_distance < distance[neigbour]:

				distance[neigbour] = new_distance
				Q.put((new_distance, neigbour))

	memo[key] = distance[end]
	return memo[key]

with open('input') as file:
	data = file.read().splitlines()

r = 0

numeric_pad = [
	'789',
	'456',
	'123',
	'.0A'
]

directional_pad = [
	'.^A',
	'<v>'
]

add_border(numeric_pad, '.', 1)
add_border(directional_pad, '.', 1)

r = 0
memo = {}
for code in data:
	length = 0
	length += get_len_shortest_path_numerical('A', code[0], memo)
	for i in range(len(code) - 1):
		length += get_len_shortest_path_numerical(code[i], code[i+1], memo)

	r += length * int(code[:-1])

print(r)