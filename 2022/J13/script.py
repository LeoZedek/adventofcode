with open('input') as f:
	data = list(map(lambda x: x.split('\n')[0], f.readlines()))

result = 0

RIGHT_ORDER = 1
NOT_RIGHT_ORDER = 2
DONT_KNOW = 3

def compare_list(left, right):
	run_out = len(left) == 0 or len(right) == 0

	while not(run_out):
		compound_left = left.pop(0)
		compound_right = right.pop(0)

		order = compare(compound_left, compound_right)

		if order != DONT_KNOW:
			return order

		run_out = len(left) == 0 or len(right) == 0

	if run_out:
		if len(left) == 0 and len(right) == 0:
			return DONT_KNOW

		elif len(left) == 0:
			return RIGHT_ORDER

		else:
			return NOT_RIGHT_ORDER

def compare(left_compound, right_compound):
	if isinstance(left_compound, int) and isinstance(right_compound, int):

		if left_compound < right_compound:
			return RIGHT_ORDER

		elif left_compound > right_compound:
			return NOT_RIGHT_ORDER

		else:
			return DONT_KNOW

	elif isinstance(left_compound, list) and isinstance(right_compound, list):
		return compare_list(left_compound, right_compound)

	elif isinstance(left_compound, int):
		return compare_list([left_compound], right_compound)

	else:
		return compare_list(left_compound, [right_compound])

for i in range((len(data) + 1) // 3):
	left_string = data[i * 3]
	right_string = data[i * 3 + 1]

	left = eval(left_string)
	right = eval(right_string)

	if compare_list(left, right) == RIGHT_ORDER:
		result += i + 1

print(result)
