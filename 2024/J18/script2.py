MIN = 0
MAX = 70

DELTAS = {(0, 1), (0, -1), (1, 0), (-1, 0)}

def inside(row, col):
	return MIN <= row and row <= MAX and MIN <= col and col <= MAX

def get_neigbours(square, fallen_bytes):
	row, col = square
	neigbours = set()

	for delta in DELTAS:
		new_row, new_col = row + delta[0], col + delta[1]
		if inside(new_row, new_col) and not((new_row, new_col) in fallen_bytes):
			neigbours.add((new_row, new_col))

	return neigbours

def is_end_reachable(fallen_bytes):
	start_row, start_col = MIN, MIN
	end_row, end_col = MAX, MAX

	file = [(start_row, start_col)]
	distance = {(start_row, start_col): 0}

	while len(file) > 0:
		current_square = file.pop(0)

		for neigbour in get_neigbours(current_square, fallen_bytes):

			new_distance = distance[current_square] + 1

			if (neigbour[0], neigbour[1]) == (end_row, end_col):
				distance[neigbour] = new_distance
				file = []
				break

			if not(neigbour in distance):
				distance[neigbour] = new_distance
				file.append(neigbour)

	return (end_row, end_col) in distance

with open("input") as file:
	data = file.read().splitlines()

bytes_to_fall = []

for elt in data:
	bytes_to_fall.append(tuple(map(int, elt.split(','))))

found = False
search_interval = [1024, len(data)]

while not(found):
	index = (search_interval[0] + search_interval[1]) // 2
	fallen_bytes1 = bytes_to_fall[:index]
	fallen_bytes2 = bytes_to_fall[:index+1]

	passage_reachable1 = is_end_reachable(fallen_bytes1)
	passage_reachable2 = is_end_reachable(fallen_bytes2)

	if passage_reachable1 and not(passage_reachable2):
		byte = bytes_to_fall[index]
		print(str(byte[0]) + ',' + str(byte[1]))
		found = True

	if passage_reachable1 and passage_reachable2:
		search_interval = [index + 1, search_interval[1]]
	elif not(passage_reachable2) and not(passage_reachable1):
		search_interval = [search_interval[0], index - 1]