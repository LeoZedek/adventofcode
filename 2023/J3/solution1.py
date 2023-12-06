def around_symbole(tab, i, length, j):
	n = len(tab)
	m = len(tab[0])

	for i2 in range(max(i-1, 0), min(i+2, n)):
		for j2 in range(max(j-1, 0), min(j+length+1, m)):
			if not(i2 == i and j <= j2 and j2 <= j+length-1) and tab[i2][j2] != ".":
				return True

	return False

with open("input", "r") as file:
	data = file.readlines()

for i in range(len(data)):
	data[i] = data[i].strip()

result = 0

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

			if around_symbole(data, i, length, j-length):
				print(i, length, j)
				result += int(data[i][j-length:j])

		if not(find_number):
			j += 1

print(result)