from collections import defaultdict
import itertools as it

with open('input') as file:
	data = file.read().splitlines()

antennas = defaultdict(list)

for i, line in enumerate(data):
	for j, char in enumerate(line):
		if char != ".":
			antennas[char].append((i, j))

antinodes = set()
for antenna_type, positions in antennas.items():
	for pos1, pos2 in it.permutations(positions, 2):
		antinodes.add((pos2[0] + (pos2[0] - pos1[0]), pos2[1] + (pos2[1] - pos1[1])))

r = 0

for antinode in antinodes:
	if 0 <= antinode[0] and antinode[0] < len(data) and 0 <= antinode[1] and antinode[1] < len(data[0]):
		r += 1

print(r)