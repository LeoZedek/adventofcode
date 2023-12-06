f = open('input')

data = list(map(lambda x : x.split('\n')[0], f.readlines()))

f.close()

def isLeftVisible(data, i, j):

	for j2 in range(j):
		if data[i][j2] >= data[i][j]:
			return False

	return True

def isRightVisible(data, i, j):

	for j2 in range(j + 1, len(data[0])):
		if data[i][j2] >= data[i][j]:
			return False

	return True

def isTopVisible(data, i, j):

	for i2 in range(i):
		if data[i2][j] >= data[i][j]:
			return False

	return True

def isBottomVisible(data, i, j):

	for i2 in range(i + 1, len(data)):
		if data[i2][j] >= data[i][j]:
			return False

	return True

def isVisibleOutside(data, i, j):
	return isLeftVisible(data, i, j) or isRightVisible(data, i, j) or isTopVisible(data, i, j) or isBottomVisible(data, i, j)

def scoreTop(data, i, j):
	result = 0

	for i2 in range(i - 1, -1, -1):
		if data[i2][j] >= data[i][j]:
			result += 1
			return result
		result += 1

	return result

def scoreBottom(data, i, j):
	result = 0

	for i2 in range(i + 1, len(data)):
		if data[i2][j] >= data[i][j]:
			result += 1
			return result
		result += 1

	return result

def scoreLeft(data, i, j):
	result = 0

	for j2 in range(j - 1, -1, -1):
		if data[i][j2] >= data[i][j]:
			result += 1
			return result
		result += 1

	return result

def scoreRight(data, i, j):
	result = 0

	for j2 in range(j + 1, len(data[0])):
		if data[i][j2] >= data[i][j]:
			result += 1
			return result
		result += 1

	return result

def scenicScore(data, i, j):

	return scoreTop(data, i, j) * scoreBottom(data, i, j) * scoreLeft(data, i, j) * scoreRight(data, i, j)

n, p = len(data), len(data[0])

result1 = 0

for i in range(n):
	for j in range(p):

		if i == 0 or i == n - 1 or j == 0 or j == p - 1:
			result1 += 1

		elif isVisibleOutside(data, i, j):
			result1 += 1

print("result part 1 : ", str(result1))

scoreMax = 0

for i in range(n):
	for j in range(p):

		score = scenicScore(data, i, j)

		if score > scoreMax:
			scoreMax = score

print("result part 2 : ", scoreMax)
