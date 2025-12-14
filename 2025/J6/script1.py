def performOperation(a, b, op):
	if op == "+":
		return a + b
	else:
		return a * b

with open('input', 'r') as file:
	data = file.read().splitlines()
	for i in range(len(data)):
		data[i] = data[i].split()

result = 0

for j in range(len(data[0])):
	operation = data[-1][j]

	individualResult = 0 if operation == "+" else 1

	for i in range(len(data) - 1):
		individualResult = performOperation(individualResult, int(data[i][j]), operation)

	result += individualResult

print(result)