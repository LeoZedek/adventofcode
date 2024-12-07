import itertools as it
import math

with open('input') as file:
	data = file.readlines()

r = 0

for line in data:
	test_value, numbers = line.split(": ")
	test_value = int(test_value)
	numbers = list(map(int, numbers.split()))

	for operators in it.product("+*|", repeat=len(numbers)-1):
		value = numbers[0]

		for i in range(len(operators)):
			if operators[i] == '+':
				value += numbers[i+1]
			elif operators[i] == '*':
				value *= numbers[i+1]
			else:
				value = value * (10**(int(math.log10(numbers[i+1])) + 1)) + numbers[i+1]

			if value > test_value:
				break

		if value == test_value:
			r += value
			break

print(r)