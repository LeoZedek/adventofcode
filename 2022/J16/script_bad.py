with open('input_test') as f:
	data = f.readlines()

class Valve():

	def __init__(self, name, flow_rate):
		self.name = name
		self.flow_rate = flow_rate
		self.open = False

		self.next_valves = set()

	def add_next_valve(self, valve):
		self.next_valves.add(valve)

	def open_valve(self):
		self.open = True
		return self.flow_rate

	def copy(self):
		valve_copy = Valve(self.name, self.flow_rate)
		if self.open:
			valve.open_valve()

		return valve_copy

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

def copy_valves(valves):
	copy = valves.copy()
	for valve_name in copy.keys():
		copy[valve_name] = copy[valve_name].copy()

	for valve in copy:
		old_next_valves = valve.next_valve
		valve.next_valve = set()

		for old_valve in old_next_valve:
			valve.add_next_valve(copy[old_valve.name])

	return copy

first_valve = valves[data[0].split(' ')[1]]

valves_open = set()

def max_flow_oppening(minutes_remaining, valves, current_valves, valves_open, memo):
	if minutes_remaining == 0:
		return 0
	#print(current_valves.flow_rate)
	score = (minutes_remaining - 1) * current_valves.flow_rate

	valves_open.add(current_valves)

	score += max_flow(minutes_remaining - 1, valves, current_valves, valves_open, memo)

	return score

memo = {}

def max_flow(minutes_remaining, valves, current_valves, valves_open, memo):
	key = str(minutes_remaining) + ", " + current_valves.name
	for valve in valves_open:
		key += ", " + valve.name

	if key in memo.keys():
		return memo[key]

	if minutes_remaining == 0:
		return 0

	valves_open = valves_open.copy()
	score_max = 0

	for valve_to_visite in current_valves.next_valves:
		score_temp = max_flow(minutes_remaining - 1, valves, valve_to_visite, valves_open, memo)

		if score_temp > score_max:
			score_max = score_temp

	if not(current_valves in valves_open):
		score_temp = max_flow_oppening(minutes_remaining, valves, current_valves, valves_open, memo)

		if score_temp > score_max:
			score_max = score_temp

	memo[key] = score_max
	return memo[key]
print(first_valve.flow_rate)

print(max_flow(30, valves, first_valve, valves_open, memo))