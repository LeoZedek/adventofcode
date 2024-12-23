from queue import PriorityQueue
from collections import defaultdict

UP = 0
RIGHT = 1
LEFT = 2
DOWN = 3

DIRECTIONS = [UP, RIGHT, LEFT, DOWN]

DELTAS = {
	RIGHT: (0, 1),
	LEFT: (0, -1),
	DOWN: (1, 0),
	UP: (-1, 0)
}

with open('input') as file:
	_map = file.read().splitlines()

for i in range(len(_map)):
	for j in range(len(_map[i])):
		if _map[i][j] == 'S':
			start_row, start_col = i, j
		elif _map[i][j] == 'E':
			end_row, end_col = i, j

def get_possible_seats(node):
	possible_seats.add((node[0], node[1]))

	for previous_node in previous[node]:
		get_possible_seats(previous_node)

def get_neigbours(node):
	i, j, direction = node
	neigbours = set()

	for other_direction in DIRECTIONS:
		if other_direction != direction:
			neigbours.add((i, j, other_direction))

	delta = DELTAS[direction]
	new_i, new_j = i + delta[0], j + delta[1]

	if _map[new_i][new_j] != '#':
		neigbours.add((new_i, new_j, direction))

	return neigbours

def distance_between(node1, node2):
	return 1 if node1[2] == node2[2] else 1000

Q = PriorityQueue()
start = (start_row, start_col, RIGHT)

Q.put((0, start))

distance = {start : 0}
previous = defaultdict(set)

while not(Q.empty()):
	current_node = Q.get()[1]

	for neigbour in get_neigbours(current_node): ## get_neigbour to define

		new_distance = distance[current_node] + distance_between(current_node, neigbour) ## Distance between neigbour and current_node

		if not(neigbour in distance) or new_distance <= distance[neigbour]:
			if not(neigbour in distance) or new_distance < distance[neigbour]:
				previous[neigbour] = {current_node}
			else:
				previous[neigbour].add(current_node)
			distance[neigbour] = new_distance
			Q.put((new_distance, neigbour))

possible_seats = {(start_row, start_col), (end_row, end_col)}

for direction in DIRECTIONS:
	get_possible_seats((end_row, end_col, direction))

print(len(possible_seats))