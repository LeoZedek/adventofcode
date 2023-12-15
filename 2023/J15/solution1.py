with open("input", "r") as file:
	line = file.readline().strip()

steps = line.split(",")

result = 0

for step in steps:

	value = 0

	for char in step:
		value += ord(char)
		value *= 17
		value %= 256

	result += value

print(result)