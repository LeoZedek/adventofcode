def transform(matrix):
	result = []
	for j in range(len(matrix[0])):
		heights = -1
		for i in range(len(matrix)):
			heights += matrix[i][j] == '#'
		result.append(heights)

	return tuple(result)

def is_fit(key, lock):
	for i in range(len(key)):
		if key[i] + lock[i] > 5:
			return False

	return True

with open('input') as file:
	data = file.read().splitlines()

keys = set()
locks = set()

for i in range(0, len(data), 8):
	if data[i] == "#" * len(data[i]):
		locks.add(transform(data[i:i+7]))
	else:
		keys.add(transform(data[i:i+7]))

r = 0

for key in keys:
	for lock in locks:
		r += is_fit(key, lock)

print(r)