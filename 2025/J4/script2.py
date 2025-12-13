def isLiftable(i, j):
	numberAround = 0

	for i2 in range(i-1, i+2):
		for j2 in range(j-1, j+2):
			if ((i2 != i or j2 != j) and (0 <= i2 and i2 < h) and (0 <= j2 and j2 < w) and data[i2][j2] == "@"):
				numberAround += 1

	return numberAround < 4

with open('input', 'r') as file:
	data = file.read().splitlines()

	for i in range(len(data)):
		data[i] = list(data[i])

h = len(data)
w = len(data[0])

result = 0
removeOne = True

while removeOne:
	removeOne = False
	for i in range(h):
		for j in range(w):
			if data[i][j] == '@' and isLiftable(i, j):
				result += 1
				removeOne = True
				data[i][j] = '.'

print(result)