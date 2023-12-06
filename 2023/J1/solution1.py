with open("input", "r") as file:
	data = file.readlines()

result = 0

for chunk in data:

	i = 0
	while not(chunk[i].isdigit()):
		i += 1

	number = chunk[i]

	i = len(chunk) - 1

	while not(chunk[i].isdigit()):
		i -= 1

	number += chunk[i]

	result += int(number)

print(result)