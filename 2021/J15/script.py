import math

f = open('input')

data = f.readlines()

f.close()

for i in range(len(data)):
	data[i] = data[i].split('\n')[0]
	
tab = data

maxX = len(data[0]) - 1
maxY = len(data) - 1

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