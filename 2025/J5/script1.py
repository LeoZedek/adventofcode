def isFresh(ingredient):
	for freshRange in freshRanges:
		if (freshRange[0] <= ingredient and ingredient <= freshRange[1]):
			return True

	return False

with open('input', 'r') as file:
	data = file.read().splitlines()

freshRanges = []

i = 0

while data[i] != "":
	freshRanges.append(list(map(int, data[i].split('-'))))
	i += 1

i += 1

ingredients = []

while i < len(data):
	ingredients.append(int(data[i]))
	i += 1

result = 0

for ingredient in ingredients:
	if isFresh(ingredient):
		result += 1

print(result)
