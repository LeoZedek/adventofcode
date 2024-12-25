from collections import defaultdict
from itertools import permutations, combinations

def is_all_connected(connections_sized):
	for computer2, computer3 in combinations(connections_sized, 2):
		if not(computer2 in graph[computer3]):
			return False

	return True

def print_result(computer, connections):
	result = [computer]
	for computer in connections:
		result.append(computer)
	result.sort()
	print(','.join(result))

with open('input') as file:
	data = file.read().splitlines()

graph = defaultdict(set)

for line in data:
	computer1, computer2 = line.split('-')

	graph[computer1].add(computer2)
	graph[computer2].add(computer1)

found = False
size = 13

while not(found):

	for computer, connections in graph.items():
		for connections_sized in combinations(connections, size):
			if is_all_connected(connections_sized):
				found = True
				print_result(computer, connections_sized)

		if found:
			break


	size -= 1