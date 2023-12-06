with open('input') as f:
	data = f.readlines()

class Valve():

	def __init__(self, name, flow_rate):
		self.name = name
		self.flow_rate = flow_rate

		self.next_valves = set()

	def add_next_valve(self, valve):
		self.next_valves.add(valve)

valves = {}

for ind, string in enumerate(data):
	string_list = string.split(' ')
	name_new_valve = string_list[1]
	flow_rate = int(string_list[4][5 : -1])

	valves[name_new_valve] = Valve(name_new_valve, flow_rate)

for ind, string in enumerate(data):

	string_list = string.split(' ')
	name_valve = string_list[1]
	valve = valves[name_valve]

	for name_next_valve in list(map(lambda x: x[: -1], string_list[9 :])):
		valve.add_next_valve(valves[name_next_valve])

first_valve = valves["AA"]

valves_open = set()
valves_to_open = set()

for valve in valves.values():
	if valve.flow_rate > 0:
		valves_to_open.add(valve)

memo = {}

def max_flow(minutes_remaining, valves, current_valves, valves_open, pressure, memo):

	if minutes_remaining == 1:
		return pressure

	if len(valves_to_open) == len(valves_open):
		return pressure * minutes_remaining

	key = str(minutes_remaining) + current_valves.name + str(pressure)
	hash_code_valve_open = 0
	for valve in valves_open:
		hash_code_valve_open += hash(valve.name)

	key += str(hash_code_valve_open)

	if key in memo.keys():
		return memo[key]

	valves_open = valves_open.copy()

	score_max = -1

	for valve_to_visited in current_valves.next_valves:

		score_temp = pressure + max_flow(minutes_remaining - 1, valves, valve_to_visited, valves_open, pressure, memo)

		if score_temp > score_max:
			score_max = score_temp

	if current_valves in valves_to_open and not(current_valves in valves_open):
		valves_open.add(current_valves)

		new_pressure = pressure + current_valves.flow_rate

		score_temp = pressure + max_flow(minutes_remaining - 1, valves, current_valves, valves_open, new_pressure, memo)

		if score_temp > score_max:
			score_max = score_temp


	memo[key] = score_max
	return memo[key]

# for valve in valves.values():
# 	print(valve.name, valve.flow_rate, end = " ")

# 	for valve_new in valve.next_valves:
# 		print(valve_new.name, end= ", ")

# 	print()

print(max_flow(30, valves, first_valve, valves_open, 0, memo))