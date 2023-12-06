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

##################ALGORITHME##################################

def inserer(tab, pos, elt):
	tab = list(tab)
	tab.append(0);

	for i in range(len(tab) - 1, pos, -1):
		tab[i] = tab[i - 1]

	tab[pos] = elt
	tab = "".join(tab)

	return tab


for i in range(10):
	i = 0
	while i < len(polymer) - 1:
		key = polymer[i] + polymer[i + 1]
		if key in regles.keys():
			i += 1
			polymer = inserer(polymer, i, regles[key])

		i += 1


elementDistinct = []

for i in range(len(polymer)):
	if not(polymer[i] in elementDistinct):
		elementDistinct.append(polymer[i])

nbElement = {}

for elt in elementDistinct:
	r = 0

	for i in range(len(polymer)):
		if elt == polymer[i]:
			r += 1

	nbElement[elt] = r

import numpy as np

print(np.max(list(nbElement.values())) - np.min(list(nbElement.values())))
