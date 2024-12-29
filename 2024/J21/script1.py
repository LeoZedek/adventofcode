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
	'9': (1, 3)
}

A_directional_pad_pos = (1, 3)


DELTAS = {
	RIGHT: (0, 1),
	UP: (-1, 0),
	DOWN: (1, 0),
	LEFT: (0, -1)
}

def get_neigbours(current_node):
	pos_numerical, pos_robot_radiation, pos_robot_cold = current_node
	neigbours = set()

	# <, >, v, ^ actions
	for delta in DELTAS.values():
		new_robot_cold_row, new_robot_cold_col = pos_robot_cold[0] + delta[0], pos_robot_cold[1] + delta[1]
		if directional_pad[new_robot_cold_row][new_robot_cold_col] != '.':
			neigbours.add((pos_numerical, pos_robot_radiation, (new_robot_cold_row, new_robot_cold_col)))

	# A action
	if directional_pad[pos_robot_cold[0]][pos_robot_cold[1]] == 'A':
		if directional_pad[pos_robot_radiation[0]][pos_robot_radiation[1]] != 'A':
			delta = DELTAS[directional_pad[pos_robot_radiation[0]][pos_robot_radiation[1]]]
			new_numerical_row, new_numerical_col = pos_numerical[0] + delta[0], pos_numerical[1] + delta[1]
			if numeric_pad[new_numerical_row][new_numerical_col] != '.':
				neigbours.add(((new_numerical_row, new_numerical_col), pos_robot_radiation, pos_robot_cold))

	else:
		delta = DELTAS[directional_pad[pos_robot_cold[0]][pos_robot_cold[1]]]
		new_robot_rad_row, new_robot_rad_col = pos_robot_radiation[0] + delta[0], pos_robot_radiation[1] + delta[1]
		if directional_pad[new_robot_rad_row][new_robot_rad_col] != '.':
			neigbours.add((pos_numerical, (new_robot_rad_row, new_robot_rad_col), pos_robot_cold))

	return neigbours


def shortest(start, end):
	Q = PriorityQueue()

	Q.put((0, start))

	distance = {
		start : 0
	}
	previous = defaultdict(set) ## To get the all the shortest path (not mandatory)

	while not(Q.empty()):
		current_node = Q.get()[1]

		for neigbour in get_neigbours(current_node): ## get_neigbour to define

			new_distance = distance[current_node] + 1

			if not(neigbour in distance) or new_distance <= distance[neigbour]:
				## Shortest path save (not mandatory)
				if not(neigbour in distance) or new_distance < distance[neigbour]:
					previous[neigbour] = {current_node}
				else:
					previous[neigbour].add(current_node)

				distance[neigbour] = new_distance
				if neigbour == end:
					return distance[neigbour]
				Q.put((new_distance, neigbour))

def add_border(matrix, char, width):
	for i in range(len(matrix)):
		matrix[i] = char * width + matrix[i] + char * width

	matrix.append(char * len(matrix[0]))
	matrix.insert(0, char * len(matrix[0]))

def get_len_shortest_path_numerical(char1, char2):
	start_numerical = POSITIONS[char1]
	end_numerical = POSITIONS[char2]
	return shortest((start_numerical, A_directional_pad_pos, A_directional_pad_pos), (end_numerical, A_directional_pad_pos, A_directional_pad_pos))

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

for code in data:
	length = 0
	length += get_len_shortest_path_numerical('A', code[0]) + 1
	for i in range(len(code) - 1):
		length += get_len_shortest_path_numerical(code[i], code[i+1]) + 1
	
	r += length * int(code[:-1])

print(r)