from collections import defaultdict
from itertools import permutations, combinations

with open('input') as file:
	data = file.read().splitlines()

graph = defaultdict(set)

for line in data:
	computer1, computer2 = line.split('-')

	graph[computer1].add(computer2)
	graph[computer2].add(computer1)

r = 0

for computer1, connections in graph.items():
	for computer2, computer3 in combinations(connections, 2):
		if (computer1[0] == 't' or computer2[0] == 't' or computer3[0] == 't') and computer2 in graph[computer3]:
			r += 1

print(r // 3)