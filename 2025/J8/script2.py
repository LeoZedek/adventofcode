import math

def distance(a, b):
	return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2 + (b[2] - a[2])**2)

with open('input', 'r') as file:
	data = file.read().splitlines()

for i in range(len(data)):
	data[i] = tuple(map(int, data[i].split(',')))

couples = []

for i in range(len(data)):
	for j in range(i + 1, len(data)):
		couples.append((data[i], data[j]))

couples.sort(key = lambda x: distance(x[0], x[1]))

circuits = []

iCouple = 0
while (len(circuits) == 0 or len(circuits[0]) < len(data)):
	couple = couples[iCouple]
	circuit1 = None
	circuit2 = None

	for circuit in circuits:
		if couple[0] in circuit:
			circuit1 = circuit
		if couple[1] in circuit:
			circuit2 = circuit

	if circuit1 != circuit2:
		if circuit1 is not None and circuit2 is not None:
			circuits.remove(circuit1)
			circuits.remove(circuit2)
			circuits.append(circuit1.union(circuit2))
		elif circuit1 is not None:
			circuit1.add(couple[1])
		elif circuit2 is not None:
			circuit2.add(couple[0])

	elif circuit1 == None and circuit2 == None:
		circuits.append({couple[0], couple[1]})

	iCouple += 1

print(couple[0][0] * couple[1][0])
