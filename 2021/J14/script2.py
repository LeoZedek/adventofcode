####################DATA READING############################
f = open('input');

data = f.readlines();

f.close();

polymer = data[0].split("\n")[0];

tabRegle = []
for i in range(len(data) - 2):
	tabRegle.append(data[i + 2].split('\n')[0]);

regles = {};

for i in range(len(tabRegle)):
	key, val = tabRegle[i].split(' -> ')
	regles[key] = val

elements0 = {}

elementDistinct = []

for element in polymer:
	if not(element in elementDistinct):
		elementDistinct.append(element)

for element in regles.values():
	if not(element in elementDistinct):
		elementDistinct.append(element)

for elt in elementDistinct:
	elements0[elt] = 0


##################ALGORITHME##################################

def nbEltR(e1, e2, hauteur, memo):
	elements = elements0.copy()
	keyMemo = e1 + e2 + ',' + str(hauteur)

	if keyMemo in memo.keys():
		return memo[keyMemo]

	if hauteur == 0:

		elements[e1] += 1
		elements[e2] += 1
		memo[keyMemo] = elements
		return memo[keyMemo]

	if ((e1 + e2) in regles.keys()):
		nvElt = regles[e1 + e2]

		elements1 = nbEltR(e1, nvElt, hauteur - 1, memo)

		for key in elements.keys():
			elements[key] += elements1[key]

		elements2 = nbEltR(nvElt, e2, hauteur - 1, memo)

		for key in elements.keys():
			elements[key] += elements2[key]

		elements[nvElt] -= 1

		memo[keyMemo] = elements
		return memo[keyMemo]

	memo[keyMemo] = elements
	return memo[keyMemo]

elements = elements0.copy()
memo = {}

for i in range(len(polymer) - 1):
	nvElts = nbEltR(polymer[i], polymer[i + 1], 40, memo)

	for key in elements.keys():
		elements[key] += nvElts[key];

	if i != 0:
		elements[polymer[i]] -= 1

import numpy as np

print(np.max(list(elements.values())) - np.min(list(elements.values())))

