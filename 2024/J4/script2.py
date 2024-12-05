with open('input') as file:
	data = file.readlines()

r = 0

for i, line in enumerate(data):
	for j, char in enumerate(line):

		if char == 'A' and i > 0 and i < len(data) - 1 and j > 0 and j < len(line) - 1:
			if ((data[i-1][j-1] == 'M' and data[i+1][j+1] == 'S') or (data[i-1][j-1] == 'S' and data[i+1][j+1] == 'M')) \
			and ((data[i-1][j+1] == 'M' and data[i+1][j-1] == 'S') or (data[i-1][j+1] == 'S' and data[i+1][j-1] == 'M')):
			   r += 1

print(r)