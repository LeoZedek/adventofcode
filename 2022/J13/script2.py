with open('input') as f:
	data = list(map(lambda x: x.split('\n')[0], f.readlines()))

result = 0

RIGHT_ORDER = 1
NOT_RIGHT_ORDER = 2
DONT_KNOW = 3

def compare_list(left, right):
	i = 0
	run_out = len(left) == i or len(right) == i

	while not(run_out):
		compound_left = left[i]
		compound_right = right[i]
		i += 1

		order = compare(compound_left, compound_right)

		if order != DONT_KNOW:
			return order

		run_out = len(left) == i or len(right) == i

	if run_out:
		if len(left) == i and len(right) == i:
			return DONT_KNOW

		elif len(left) == i:
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

def sort_packets(packets):
	lenght = len(packets)

	for i in range(lenght - 1, 0, -1):
		for j in range(i):
			if compare_list(packets[j], packets[j + 1]) == NOT_RIGHT_ORDER:
				packets[j + 1], packets[j] = packets[j], packets[j + 1]

	return packets

packets = []

for ind, string in enumerate(data):
	if string != "":
		packets.append(eval(string))

divider_packet1 = [[2]]
divider_packet2 = [[6]]

packets.append([[2]])
packets.append([[6]])

packets = sort_packets(packets)
result = 1
for ind, packet in enumerate(packets):
	if packet == divider_packet2 or packet == divider_packet1:
		result *= ind + 1

print(result)
