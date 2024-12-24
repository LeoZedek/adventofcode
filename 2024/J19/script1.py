def number_arrangement(towel, memo):
	if towel == '':
		return 1

	if towel in memo:
		return memo[towel]

	result = 0

	for pattern in available_patterns:
		if len(pattern) <= len(towel) and pattern == towel[:len(pattern)]:
			result += number_arrangement(towel[len(pattern):], memo)

	memo[towel] = result
	return memo[towel]


with open('input') as file:
	available_patterns = file.readline().strip().split(', ')
	file.readline()

	towel = file.readline().strip()
	towels = set()
	while towel != '':
		towels.add(towel)
		towel = file.readline().strip()

r = 0
memo = {}
for towel in towels:
	if number_arrangement(towel, memo) > 0:
		r += 1

print(r)