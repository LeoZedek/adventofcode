def update_gear(tab, i, length, j, gear, number):
	n = len(tab)
	m = len(tab[0])

	for i2 in range(max(i-1, 0), min(i+2, n)):
		for j2 in range(max(j-1, 0), min(j+length+1, m)):
			if not(i2 == i and j <= j2 and j2 <= j+length-1) and tab[i2][j2] == "*":
				if not((i2, j2) in gear):
					gear[(i2, j2)] = [number]
				else:
					gear[(i2, j2)].append(number)

with open("input", "r") as file:
	data = file.readlines()

for i in range(len(data)):
	data[i] = data[i].strip()

gear = {}

for i in range(len(data)):
	j = 0
	while j < len(data[i]):
		find_number = False

		char = data[i][j]

		length = 0

		if char.isdigit():

			while j < len(data[i]) and data[i][j].isdigit():
				find_number = True
				length += 1
				j += 1

			update_gear(data, i, length, j-length, gear, int(data[i][j-length:j]))

		if not(find_number):
			j += 1

result = 0

for item in gear.values():
	if len(item) == 2:
		result += item[0]*item[1]

print(result)