from collections import defaultdict
import itertools as it

with open('input') as file:
	data = file.read().splitlines()

def fill_diagonal(pos, di, dj):
	i = 0
	while 0 <= pos[0] + i*di and pos[0] + i*di < len(data) and 0 <= pos[1] + i*dj and pos[1] + i*dj < len(data[0]):
		antinodes.add((pos[0] + i*di, pos[1] + i*dj))
		i += 1

antennas = defaultdict(list)

for i, line in enumerate(data):
	for j, char in enumerate(line):
		if char != ".":
			antennas[char].append((i, j))

antinodes = set()
for antenna_type, positions in antennas.items():
	for pos1, pos2 in it.permutations(positions, 2):

		if pos1[0] == pos2[0]:
			for j in range(len(data[0])):
				antinodes.add((pos1[0], j))

		elif pos1[1] == pos2[1]:
			for i in range(len(data)):
				antinodes.add((i, pos1[1]))

		elif abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1]):
			if (pos1[0] - pos2[0]) * (pos1[1] - pos2[1]) > 0:
				fill_diagonal(pos1, 1, 1)
				fill_diagonal(pos1, -1, -1)
			else:
				fill_diagonal(pos1, -1, 1)
				fill_diagonal(pos1, 1, -1)

		else:

			i = 0
			while 0 <= pos2[0] + i*(pos2[0] - pos1[0]) and pos2[0] + i*(pos2[0] - pos1[0]) < len(data) and\
				0 <= pos2[1] + i*(pos2[1] - pos1[1]) and pos2[1] + i*(pos2[1] - pos1[1]) < len(data[0]):

				antinodes.add((pos2[0] + i*(pos2[0] - pos1[0]), pos2[1] + i*(pos2[1] - pos1[1])))
				i += 1

r = 0

for antinode in antinodes:
	if 0 <= antinode[0] and antinode[0] < len(data) and 0 <= antinode[1] and antinode[1] < len(data[0]):
		r += 1

print(r)