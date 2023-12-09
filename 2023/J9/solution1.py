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

	last_values = {}

	last_values[0] = history[-1]

	number_history = 1

	while not(all_zeros(history)):

		new_history = []

		for i in range(len(history) - 1):
			new_history.append(history[i+1] - history[i])

		history = new_history

		last_values[number_history] = history[-1]

		number_history += 1

	next_value = 0

	for i in range(number_history - 1, -1, -1):

		next_value += last_values[i]

	result += next_value

print(result)