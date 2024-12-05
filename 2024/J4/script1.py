with open('input') as file:
	data = file.readlines()

r = 0

for i, line in enumerate(data):
	for j, char in enumerate(line):

		if char == 'X':
			if j < len(line) - 3:
				r += line[j+1:j+4] == 'MAS'

				if i >= 3:
					r += (data[i-1][j+1] + data[i-2][j+2] + data[i-3][j+3]) == 'MAS'
				if i < len(data) - 3:
					r += (data[i+1][j+1] + data[i+2][j+2] + data[i+3][j+3]) == 'MAS'


			if j >= 3:
				r += line[j-3:j] == 'SAM'

				if i >= 3:
					r += (data[i-1][j-1] + data[i-2][j-2] + data[i-3][j-3]) == 'MAS'
				if i < len(data) - 3:
					r += (data[i+1][j-1] + data[i+2][j-2] + data[i+3][j-3]) == 'MAS'

			if i >= 3:
				r += (data[i-1][j] + data[i-2][j] + data[i-3][j]) == 'MAS'

			if i < len(data) - 3:
				r += (data[i+1][j] + data[i+2][j] + data[i+3][j]) == 'MAS'

print(r)