DELTAS = {
	(0, 1),
	(0, -1),
	(1, 0),
	(-1, 0)
}

def get_delta_cheats(lenght):
	delta_cheats = set()

	for di in range(-lenght, lenght + 1):
		for dj in range(-lenght + abs(di), lenght - abs(di) + 1):
			if abs(di) + abs(dj) <= lenght:
				delta_cheats.add((di, dj))

	return delta_cheats

def get_possible_cheat(path, distance, row, col, threshold, delta_cheats):
	result = set()

	for delta in delta_cheats:
		end_cheat = (row + delta[0], col + delta[1])
		time_cheat = abs(delta[0]) + abs(delta[1])
		if end_cheat in path and (distance[end_cheat] - distance[(row, col)] - time_cheat >= threshold):
			result.add(((row, col), end_cheat))

	return result


def get_neigbours(data, square):
	row, col = square
	neigbours = set()

	for delta in DELTAS:
		new_row, new_col = row + delta[0], col + delta[1]
		if not(data[new_row][new_col] == '#'):
			neigbours.add((new_row, new_col))

	return neigbours

def main():

	with open('input') as file:
		data = file.read().splitlines()

	for i in range(len(data)):
		for j in range(len(data[i])):
			if data[i][j] == 'S':
				start_row, start_col = i, j
			elif data[i][j] == 'E':
				end_row, end_col = i, j

	file = [(start_row, start_col)]
	distance = {(start_row, start_col): 0}
	previous = {}

	while len(file) > 0:
		current_square = file.pop(0)

		for neigbour in get_neigbours(data, current_square):

			new_distance = distance[current_square] + 1

			if (neigbour[0], neigbour[1]) == (end_row, end_col):
				distance[neigbour] = new_distance
				previous[neigbour] = current_square
				file = []
				break

			if not(neigbour in distance):
				distance[neigbour] = new_distance
				previous[neigbour] = current_square
				file.append(neigbour)

	path = set()
	path = {(end_row, end_col)}
	square = (end_row, end_col)

	while square in previous:
		square = previous[square]
		path.add(square)

	delta_cheats = get_delta_cheats(20)
	r = 0
	for (i, j) in path:
		r += len(get_possible_cheat(path, distance, i, j, 100, delta_cheats))
	print(r)

if __name__ == '__main__':
	main()