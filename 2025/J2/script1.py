with open('input', 'r') as files:
	data = files.readline().replace('\n', '').split(',')

result = 0

for ranges in data:
	range1, range2 = ranges.split('-')

	if len(range1) % 2 == 0:
		midRange1 = range1[:len(range1) // 2]
		firstDouble = int(midRange1) * 10 ** len(midRange1) + int(midRange1)
		if firstDouble < int(range1):
			firstDouble = (int(midRange1) + 1) * 10 ** len(midRange1) + int(midRange1) + 1
	else:
		firstDouble = 10 ** (len(range1)) + 10 ** (len(range1) // 2)

	if len(range2) % 2 == 0:
		midRange2 = range2[:len(range2) // 2]
		secondDouble = int(midRange2) * 10 ** len(midRange2) + int(midRange2)
		if secondDouble > int(range2):
			secondDouble = (int(midRange2) - 1) * 10 ** len(midRange2) + int(midRange2) - 1
	else:
		secondDouble = 0
		for power in range(len(range2) - 1):
			secondDouble += 9 * 10 ** power

	if (firstDouble <= secondDouble):
		firstInvalidId = int(str(firstDouble)[:len(str(firstDouble)) // 2])
		secondInvalidId = int(str(secondDouble)[:len(str(secondDouble)) // 2])

		for invalidId in range(firstInvalidId, secondInvalidId + 1):
			result += invalidId * 10 ** len(str(invalidId)) + invalidId


print(result)
