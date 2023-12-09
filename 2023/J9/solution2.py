def all_zeros(l):
	for elt in l:
		if elt != 0:
			return False

	return True


with open('input', 'r') as file:
	data = file.readlines()

result = 0

for line in data:

	history = list(map(int, line.split()))

	first_values = {}

	first_values[0] = history[0]

	number_history = 1

	while not(all_zeros(history)):

		new_history = []

		for i in range(len(history) - 1):
			new_history.append(history[i+1] - history[i])

		history = new_history

		first_values[number_history] = history[0]

		number_history += 1

	next_value = 0

	for i in range(number_history - 1, -1, -1):

		next_value = first_values[i] - next_value

	result += next_value

print(result)