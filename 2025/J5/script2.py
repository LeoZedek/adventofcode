## Is r1 include in r2
def isIncludeIn(r1, r2):
	return r2[0] <= r1[0] and r1[0] <= r2[1] and r2[0] <= r1[1] and r1[1] <= r2[1]

def haveOverlap(r1, r2):
	return not( r1[1] < r2[0] or r2[1] < r1[0] )

with open('input', 'r') as file:
	data = file.read().splitlines()

freshRanges = []

i = 0

while data[i] != "":
	freshRanges.append(list(map(int, data[i].split('-'))))
	i += 1

for i in range(len(freshRanges)):
	range1 = freshRanges[i]

	for j in range(i + 1, len(freshRanges)):
		range2 = freshRanges[j]

		if haveOverlap(range1, range2):

			if isIncludeIn(range1, range2):
				freshRanges[i] = [-1, -2]
			elif isIncludeIn(range2, range1):
				freshRanges[j] = [-1, -2]
			else:
				minRange = min([range1, range2], key = lambda x: x[0])
				maxRange = range1 if minRange == range2 else range2
				if minRange[1] >= maxRange[0]:
					maxRange[0] = minRange[1] + 1

sumRange = 0

for freshRange in freshRanges:
	sumRange += freshRange[1] - freshRange[0] + 1

print(sumRange)