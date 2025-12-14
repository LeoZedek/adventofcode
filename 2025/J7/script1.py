with open('input', 'r') as file:
	data = file.read().splitlines()

newTachyons = set()
result = 0

for i in range(len(data)):
	for j in range(len(data[0])):
		if data[i][j] == "S":
			newTachyons.add((i, j))

hasMoved = True

while hasMoved:
	hasMoved = False
	tachyons = newTachyons.copy()
	newTachyons = set()
	for tachyon in tachyons:
		if tachyon[0] < len(data) - 1:
			hasMoved = True
			if data[tachyon[0] + 1][tachyon[1]] == '^':
				result += 1
				newTachyons.add((tachyon[0] + 1, tachyon[1] - 1))
				newTachyons.add((tachyon[0] + 1, tachyon[1] + 1))
			else:
				newTachyons.add((tachyon[0] + 1, tachyon[1]))

print(result)