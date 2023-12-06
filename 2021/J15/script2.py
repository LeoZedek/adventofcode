import math

f = open('input')

data = f.readlines()

f.close()

for i in range(len(data)):
	data[i] = data[i].split('\n')[0]
	
tailleX = len(data)
tailleY = len(data[0])

for k in range(4):
	a = len(data) - tailleX
	b = len(data)
	for i in range(a, b):
		s = ""

		for elt in data[i]:
			if int(elt) < 9:
				s = s + str(int(elt) + 1)
			else:
				s = s + "1"

		data.append(s)

for i in range(len(data)):

	s = data[i]

	for k in range(4):
		a = len(data[i]) - tailleY
		b = len(data[i])
		for j in range(a, b):

			if int(s[j]) < 9:
				s = s + str(int(s[j]) + 1)
			else:
				s = s + "1"

		data[i] = s

tab = data

maxY = len(data[0]) - 1
maxX = len(data) - 1

marque = {}

d = {}
for i in range(maxX + 1):
	for j in range(maxY + 1):
		d[(i, j)] = math.inf
		marque[(i, j)] = False

d[(0, 0)] = 0

marque[(0, 0)] = True

def getAdjacentGraphe(previousAdjacent, marque, maxX, maxY):
	resultat = previousAdjacent.copy()

	for elt in previousAdjacent:
		if marque[elt]:
			if elt[0] + 1 <= maxX and not(marque[(elt[0] + 1, elt[1])]):
				resultat.add((elt[0] + 1, elt[1]))

			if elt[0] - 1 >= 0 and not(marque[(elt[0] - 1, elt[1])]):
				resultat.add((elt[0] - 1, elt[1]))

			if elt[1] + 1 <= maxY and not(marque[(elt[0], elt[1] + 1)]):
				resultat.add((elt[0], elt[1] + 1))

			if elt[1] - 1 >= 0 and not(marque[(elt[0], elt[1] - 1)]):
				resultat.add((elt[0], elt[1] - 1))

			resultat.remove(elt)

	return resultat

def getAdjacentPoint(marque, point, maxX, maxY):
	resultat = []

	if point[0] + 1 <= maxX and not(marque[(point[0] + 1, point[1])]):
		resultat.append((point[0] + 1, point[1]))

	if point[0] - 1 >= 0 and not(marque[(point[0] - 1, point[1])]):
		resultat.append((point[0] - 1, point[1]))

	if point[1] + 1 <= maxY and not(marque[(point[0], point[1] + 1)]):
		resultat.append((point[0], point[1] + 1))

	if point[1] - 1 >= 0 and not(marque[(point[0], point[1] - 1)]):
		resultat.append((point[0], point[1] - 1))

	return resultat


previous = {}

adjacent = set()
adjacent.add((0, 0))

while len(adjacent) > 0:

	minAdjacent = min(adjacent, key = lambda x : d[x])
	marque[minAdjacent] = True

	for b in getAdjacentPoint(marque, minAdjacent, maxX, maxY):
		if d[b] > d[minAdjacent] + int(tab[b[0]][b[1]]):
			d[b] =  d[minAdjacent] + int(tab[b[0]][b[1]])
			previous[b] = minAdjacent

	adjacent =  getAdjacentGraphe(adjacent, marque, maxX, maxY)

r = 0

r += int(tab[maxX][maxY])

prev = previous[(maxX, maxY)]

while prev != (0, 0):

	r += int(tab[prev[0]][prev[1]])
	prev = previous[prev]

print(r)