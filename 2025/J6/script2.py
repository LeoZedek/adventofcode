def performOperation(numbers, op):
	if op == "+":
		return sum(numbers)
	else:
		multiplyOp = 1
		for number in numbers:
			multiplyOp *= number
		return multiplyOp

def getNumber(j):
	number = ""

	for i in range(len(data) - 1):
		if data[i][j] != ' ':
			number += data[i][j]

	return int(number)

with open('input', 'r') as file:
	data = file.read().splitlines()

result = 0

j = len(data[0]) - 1
numbers = []

while j >= 0:
	numbers.append(getNumber(j))
	if data[-1][j] != ' ':
		operation = data[-1][j]
		result += performOperation(numbers, operation)
		numbers = []
		j -= 1

	j -= 1

print(result)