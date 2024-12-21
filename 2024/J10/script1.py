DELTAS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def compute_tops(i, j, height):
	if height == 9:
		tops.add((i, j))

	score = 0

	for delta in DELTAS:
		new_i = i + delta[0]
		new_j = j + delta[1]

		if data[new_i][new_j] != '.' and int(data[new_i][new_j]) == height + 1:
			score += compute_tops(new_i, new_j, height + 1)

	return score

with open('input') as file:
	data = file.read().splitlines()

for i in range(len(data)):
	data[i] = '.' + data[i] + '.'

data.append('.' * len(data[0]))
data.insert(0, '.' * len(data[0]))

r = 0

for i in range(len(data)):
	for j in range(len(data[i])):
		if data[i][j] == '0':
			tops = set()
			compute_tops(i, j, 0)
			r += len(tops)

print(r)