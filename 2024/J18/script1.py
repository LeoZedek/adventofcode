MIN = 0
MAX = 70

DELTAS = {(0, 1), (0, -1), (1, 0), (-1, 0)}

def inside(row, col):
	return MIN <= row and row <= MAX and MIN <= col and col <= MAX

def get_neigbours(square):
	row, col = square
	neigbours = set()

	for delta in DELTAS:
		new_row, new_col = row + delta[0], col + delta[1]
		if inside(new_row, new_col) and not((new_row, new_col) in fallen_bytes):
			neigbours.add((new_row, new_col))

	return neigbours


with open("input") as file:
	data = file.read().splitlines()

data = data[:1024]

fallen_bytes = []

for elt in data:
	fallen_bytes.append(tuple(map(int, elt.split(','))))

start_row, start_col = MIN, MIN
end_row, end_col = MAX, MAX

file = [(start_row, start_col)]
distance = {(start_row, start_col): 0}

while len(file) > 0:
	current_square = file.pop(0)

	for neigbour in get_neigbours(current_square):

		new_distance = distance[current_square] + 1

		if (neigbour[0], neigbour[1]) == (end_row, end_col):
			print(new_distance)
			file = []
			break

		if not(neigbour in distance):
			distance[neigbour] = new_distance
			file.append(neigbour)