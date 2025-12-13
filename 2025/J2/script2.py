def isSubsequenceRepeting(number):

	for l in range(1, len(number) // 2 + 1):
		if (len(number) % l == 0):
			subSequence = number[:l]
			if (subSequence * (len(number) // l)) == number:
				return True

	return False

with open('input', 'r') as files:
	data = files.readline().replace('\n', '').split(',')

result = 0
diff = 0

for ranges in data:
	range1, range2 = list(map(int, ranges.split('-')))

	for n in range(range1, range2 + 1):
		if isSubsequenceRepeting(str(n)):
			result += n

print(result)
