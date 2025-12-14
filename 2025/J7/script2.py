def numberTimeline(i, j, memo):
	key = (i, j)
	if key in memo:
		return memo[key]

	if i == len(data) - 1:
		return 1

	if data[i + 1][j] == '^':
		res = numberTimeline(i + 1, j + 1, memo) + numberTimeline(i + 1, j - 1, memo)
	else:
		res = numberTimeline(i + 1, j, memo)

	memo[key] = res
	return res

with open('input', 'r') as file:
	data = file.read().splitlines()

for i in range(len(data)):
	for j in range(len(data[0])):
		if data[i][j] == "S":
			print(numberTimeline(i, j, {}))

