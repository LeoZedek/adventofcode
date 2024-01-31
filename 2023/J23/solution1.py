import sys

sys.setrecursionlimit(10000)

deltas = {
	(1, 0),
	(-1, 0),
	(0, 1),
	(0, -1)
}

slope_allowed = {
	(0, 1): ">",
	(0, -1): "<",
	(1, 0): "v",
	(-1, 0): "^"
}

def is_in_bound(x, y):
	return 0 <= x and x < len(data[0]) and 0 <= y and y < len(data)

def get_longest(pos, coming_from):

	if pos == end:
		return 0

	possible_ways = set()

	for delta in deltas:
		y, x = tuple((pos[i] + delta[i] for i in range(len(delta))))

		if (y, x) != coming_from and is_in_bound(x, y):

			if data[y][x] == ".":
				possible_ways.add((y, x))
			elif data[y][x] != "#":
				if data[y][x] == slope_allowed[delta]:
					possible_ways.add((y, x))

	longest_path = -1000000

	for way in possible_ways:
		lenght = 1 + get_longest(way, pos)
		if longest_path < lenght:
			longest_path = lenght

	return longest_path

with open("input", "r") as file:
	data = file.readlines()

data = list(map(lambda x: x.strip(), data))

for j in range(len(data[0])):
	if data[0][j] == ".":
		start = (0, j)

	if data[-1][j] == ".":
		end = (len(data) - 1, j)

print(get_longest(start, (0, 0)))