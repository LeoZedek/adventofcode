import itertools

from time import time

import math

with open('input') as f:
	data = f.readlines()

class Valve():

	def __init__(self, name, flow_rate):
		self.name = name
		self.flow_rate = flow_rate

		self.next_valves = set()

	def add_next_valve(self, valve):
		self.next_valves.add(valve)

	def __repr__(self):
		return self.name

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

def min_distance(valve_depart, valve_fin):

	distance = {}
	distance[valve_depart] = 0

	queue = []
	queue.append(valve_depart)
	valve_visited = set()
	valve_visited.add(valve_depart)

	while len(queue) > 0:

		current_valve = queue.pop(0)

		for next_valve in current_valve.next_valves:
			if not(next_valve in valve_visited):
				valve_visited.add(next_valve)
				queue.append(next_valve)
				distance[next_valve] = distance[current_valve] + 1

				if next_valve == valve_fin:
					return distance[valve_fin]

	return math.inf

distance = {}

for valve_depart in valves_to_open:
	for valve_fin in valves_to_open:
		if valve_depart != valve_fin:
			distance[(valve_depart, valve_fin)] = min_distance(valve_depart, valve_fin)

for valve_fin in valves_to_open:
	distance[(first_valve, valve_fin)] = min_distance(first_valve, valve_fin)

memo = {}

def max_flow_visiting(minutes_remaining, valves_to_open, my_valve_to_visited, my_distance, elephant_valve_to_visited, distance_elephant, valves_open, pressure, memo):
	score_max = 0

	if my_distance > distance_elephant:
		minutes_to_wait = my_distance - distance_elephant

		score_temp = pressure * distance_elephant + max_flow(minutes_remaining - distance_elephant, valves_to_open, my_valve_to_visited, minutes_to_wait, elephant_valve_to_visited, 0, valves_open, pressure, memo)
		score_max = max(score_max, score_temp)

	else:
		minutes_to_wait = distance_elephant - my_distance

		score_temp = pressure * my_distance + max_flow(minutes_remaining - my_distance, valves_to_open, my_valve_to_visited, 0, elephant_valve_to_visited, minutes_to_wait, valves_open, pressure, memo)
		score_max = max(score_max, score_temp)

	return score_max

def max_flow(minutes_remaining, valves_to_open, my_current_valves, my_minutes_to_wait, elephant_current_valves, elephant_minutes_to_wait, valves_open, pressure, memo):

	if minutes_remaining <= 1:
		return pressure * minutes_remaining

	if len(valves_to_open) == len(valves_open):
		return pressure * minutes_remaining

	valves_open = valves_open.copy()

	key = str(minutes_remaining) + str(hash(my_current_valves.name + str(my_minutes_to_wait)) + hash(elephant_current_valves.name + str(elephant_minutes_to_wait)))
	hash_code_valve_open = 0
	for valve in valves_open:
		hash_code_valve_open += hash(valve.name)

	key += str(hash_code_valve_open)

	if key in memo.keys():
		return memo[key]

	# if len(valves_open) == len(valves_to_open) - 1:
	# 	last_valve_to_open = valves_to_open.difference(valves_open).pop()

	# 	if my_current_valves == last_valve_to_open or elephant_current_valves == last_valve_to_open:
	# 		return pressure + (minutes_remaining - 1) * (pressure + last_valve_to_open.flow_rate)

	# 	else:
	# 		my_distance = distance[(my_current_valves, last_valve_to_open)] + my_minutes_to_wait
	# 		elephant_distance = distance[(elephant_current_valves, last_valve_to_open)] + elephant_minutes_to_wait

	# 		min_distance = min(my_distance, elephant_distance)

	# 		if min_distance < minutes_remaining:
	# 			return pressure * (min_distance + 1) + (pressure + last_valve_to_open.flow_rate) * (minutes_remaining - min_distance - 1)
	# 		else:
	# 			return pressure * minutes_remaining

	score_max = 0

	if my_minutes_to_wait == 0 and elephant_minutes_to_wait == 0:

		if my_current_valves != elephant_current_valves:
			for my_valve_to_visited, elephant_valve_to_visited in itertools.product(valves_to_open, valves_to_open):
				if my_valve_to_visited != my_current_valves and elephant_valve_to_visited != elephant_current_valves\
				and not(my_valve_to_visited in valves_open) and not(elephant_valve_to_visited in valves_open):

					distance_elephant = distance[(elephant_current_valves, elephant_valve_to_visited)]
					my_distance = distance[(my_current_valves, my_valve_to_visited)]

					score_temp = max_flow_visiting(minutes_remaining, valves_to_open, my_valve_to_visited, my_distance, elephant_valve_to_visited, distance_elephant, valves_open, pressure, memo)
					if score_temp > score_max:
						score_max = score_temp

		else:
			for my_valve_to_visited, elephant_valve_to_visited in itertools.combinations_with_replacement(valves_to_open, 2):
				if my_valve_to_visited != my_current_valves and elephant_valve_to_visited != elephant_current_valves\
				and not(my_valve_to_visited in valves_open) and not(elephant_valve_to_visited in valves_open):
					
					distance_elephant = distance[(elephant_current_valves, elephant_valve_to_visited)]
					my_distance = distance[(my_current_valves, my_valve_to_visited)]

					score_temp = max_flow_visiting(minutes_remaining, valves_to_open, my_valve_to_visited, my_distance, elephant_valve_to_visited, distance_elephant, valves_open, pressure, memo)
					if score_temp > score_max:
						score_max = score_temp

		if my_current_valves in valves_to_open and not(my_current_valves in valves_open):
			valves_open_temp = valves_open.copy()
			valves_open_temp.add(my_current_valves)

			new_pressure = pressure + my_current_valves.flow_rate

			for elephant_valve_to_visited in valves_to_open:
				if elephant_valve_to_visited != elephant_current_valves and not(elephant_valve_to_visited in valves_open):

					elephant_minutes_to_wait = distance[(elephant_current_valves, elephant_valve_to_visited)] - 1

					score_temp = pressure + max_flow(minutes_remaining - 1, valves_to_open, my_current_valves, 0, elephant_valve_to_visited, elephant_minutes_to_wait, valves_open_temp, new_pressure, memo)

					if score_temp > score_max:
						score_max = score_temp

		if elephant_current_valves in valves_to_open and not(elephant_current_valves in valves_open) and my_current_valves != elephant_current_valves:
			valves_open_temp = valves_open.copy()
			valves_open_temp.add(elephant_current_valves)

			new_pressure = pressure + elephant_current_valves.flow_rate

			for my_valve_to_visited in valves_to_open:
				if my_current_valves != my_valve_to_visited and not(my_valve_to_visited in valves_open):

					my_minutes_to_wait = distance[(my_current_valves, my_valve_to_visited)] - 1

					score_temp = pressure + max_flow(minutes_remaining - 1, valves_to_open, my_valve_to_visited, my_minutes_to_wait, elephant_current_valves, 0, valves_open_temp, new_pressure, memo)

					if score_temp > score_max:
						score_max = score_temp

		if my_current_valves != elephant_current_valves\
		and elephant_current_valves in valves_to_open and not(elephant_current_valves in valves_open)\
		and my_current_valves in valves_to_open and not(my_current_valves in valves_open):

			valves_open_temp = valves_open.copy()
			valves_open_temp.add(my_current_valves)
			valves_open_temp.add(elephant_current_valves)

			new_pressure = pressure + elephant_current_valves.flow_rate + my_current_valves.flow_rate

			score_temp = pressure + max_flow(minutes_remaining - 1, valves_to_open, my_current_valves, 0, elephant_current_valves, 0, valves_open_temp, new_pressure, memo)

			if score_temp > score_max:
				score_max = score_temp

	elif elephant_minutes_to_wait == my_minutes_to_wait:
		score_temp = pressure * my_minutes_to_wait + max_flow(minutes_remaining - my_minutes_to_wait, valves_to_open, my_current_valves, 0, elephant_current_valves, 0, valves_open, pressure, memo)
		score_max = max(score_max, score_temp)
		print("should not happen")

	elif elephant_minutes_to_wait > 0:

		for my_valve_to_visited in valves_to_open:
			if my_valve_to_visited != my_current_valves and not(my_valve_to_visited in valves_open):

				elephant_valve_to_visited = elephant_current_valves

				distance_elephant = elephant_minutes_to_wait
				my_distance = distance[(my_current_valves, my_valve_to_visited)]

				score_temp = max_flow_visiting(minutes_remaining, valves_to_open, my_valve_to_visited, my_distance, elephant_valve_to_visited, distance_elephant, valves_open, pressure, memo)
				if score_temp > score_max:
					score_max = score_temp

		if my_current_valves in valves_to_open and not(my_current_valves in valves_open):
			valves_open_temp = valves_open.copy()
			valves_open_temp.add(my_current_valves)

			new_pressure = pressure + my_current_valves.flow_rate

			score_temp = pressure + max_flow(minutes_remaining - 1, valves_to_open, my_current_valves, 0, elephant_current_valves, elephant_minutes_to_wait - 1, valves_open_temp, new_pressure, memo)

			if score_temp > score_max:
				score_max = score_temp

	else:

		for elephant_valve_to_visited in valves_to_open:
			if elephant_current_valves != elephant_valve_to_visited and not(elephant_valve_to_visited in valves_open):
				my_valve_to_visited = my_current_valves

				distance_elephant = distance[(elephant_current_valves, elephant_valve_to_visited)]
				my_distance = my_minutes_to_wait

				score_temp = max_flow_visiting(minutes_remaining, valves_to_open, my_valve_to_visited, my_distance, elephant_valve_to_visited, distance_elephant, valves_open, pressure, memo)
				if score_temp > score_max:
					score_max = score_temp

		if elephant_current_valves in valves_to_open and not(elephant_current_valves in valves_open):
			valves_open_temp = valves_open.copy()
			valves_open_temp.add(elephant_current_valves)

			new_pressure = pressure + elephant_current_valves.flow_rate

			score_temp = pressure + max_flow(minutes_remaining - 1, valves_to_open, my_current_valves, my_minutes_to_wait - 1, elephant_current_valves, 0, valves_open_temp, new_pressure, memo)
			if score_temp > score_max:
				score_max = score_temp

	memo[key] = score_max
	return memo[key]

def max_flow_slow(minutes_remaining, valves, my_current_valves, elephant_current_valves, valves_open, pressure, memo):

	if minutes_remaining == 1:
		return pressure

	if len(valves_to_open) == len(valves_open):
		return pressure * minutes_remaining

	valves_open = valves_open.copy()

	key = str(minutes_remaining) + str(hash(my_current_valves.name) + hash(elephant_current_valves.name))
	hash_code_valve_open = 0
	for valve in valves_open:
		hash_code_valve_open += hash(valve.name)

	key += str(hash_code_valve_open)

	if key in memo.keys():
		return memo[key]

	score_max = -1

	if my_current_valves != elephant_current_valves:
		for my_valve_to_visited, elephant_valve_to_visited in itertools.product(my_current_valves.next_valves, elephant_current_valves.next_valves):

				score_temp = pressure + max_flow_slow(minutes_remaining - 1, valves, my_valve_to_visited, elephant_valve_to_visited, valves_open, pressure, memo)

				if score_temp > score_max:
					score_max = score_temp

	else:
		for my_valve_to_visited, elephant_valve_to_visited in itertools.combinations_with_replacement(my_current_valves.next_valves, 2):
			score_temp = pressure + max_flow_slow(minutes_remaining - 1, valves, my_valve_to_visited, elephant_valve_to_visited, valves_open, pressure, memo)

			if score_temp > score_max:
				score_max = score_temp

	if my_current_valves in valves_to_open and not(my_current_valves in valves_open):
		valves_open_temp = valves_open.copy()
		valves_open_temp.add(my_current_valves)

		new_pressure = pressure + my_current_valves.flow_rate

		for elephant_valve_to_visited in elephant_current_valves.next_valves:

			score_temp = pressure + max_flow_slow(minutes_remaining - 1, valves, my_current_valves, elephant_valve_to_visited, valves_open_temp, new_pressure, memo)

			if score_temp > score_max:
				score_max = score_temp

	if elephant_current_valves in valves_to_open and not(elephant_current_valves in valves_open) and my_current_valves != elephant_current_valves:
		valves_open_temp = valves_open.copy()
		valves_open_temp.add(elephant_current_valves)

		new_pressure = pressure + elephant_current_valves.flow_rate

		for my_valve_to_visited in my_current_valves.next_valves:

			score_temp = pressure + max_flow_slow(minutes_remaining - 1, valves, my_valve_to_visited, elephant_current_valves, valves_open_temp, new_pressure, memo)

			if score_temp > score_max:
				score_max = score_temp

	if my_current_valves != elephant_current_valves\
		and elephant_current_valves in valves_to_open and not(elephant_current_valves in valves_open)\
		and my_current_valves in valves_to_open and not(my_current_valves in valves_open):

		valves_open_temp = valves_open.copy()
		valves_open_temp.add(my_current_valves)
		valves_open_temp.add(elephant_current_valves)

		new_pressure = pressure + elephant_current_valves.flow_rate + my_current_valves.flow_rate

		score_temp = pressure + max_flow_slow(minutes_remaining - 1, valves, my_current_valves, elephant_current_valves, valves_open_temp, new_pressure, memo)

		if score_temp > score_max:
			score_max = score_temp

	memo[key] = score_max
	return score_max

time1 = time()

print(max_flow(26, valves_to_open, first_valve, 0, first_valve, 0, valves_open, 0, memo))
time2 = time()

memo = {}
valves_open = set()

print(max_flow_slow(26, valves, first_valve, first_valve, valves_open, 0, memo))

time3 = time()

print("temps rapide :", time2 - time1)
print("temps lent :", time3 - time2)