###########################DATA READING#############################
f = open('input')

data = f.readlines()

f.close()

for i in range(len(data)):
	data[i] = data[i].split('\n')[0].split('-')

#######################ALGORITHME##########################################

carte = {}

for chemin in data:
	for cave in chemin:
		if not(cave in carte.keys()):
			carte[cave] = []

			for chemin2 in data:
				if cave in chemin2:
					caveAdjacente = chemin2[{0 : 1, 1 : 0}[chemin2.index(cave)]]

					if not(caveAdjacente in carte[cave]):
						carte[cave].append(caveAdjacente)

def nombreDeChemins(carte, caveActuelle, memory, estPasseDeuxFois):
	if caveActuelle == 'end':
		return 1

	resultat = 0

	caveVisitees = memory.copy()
	if caveActuelle.islower() and not(caveActuelle in caveVisitees):
		caveVisitees.append(caveActuelle)

	for caveAdjacente in carte[caveActuelle]:
		if not(caveAdjacente in caveVisitees):
			resultat += nombreDeChemins(carte, caveAdjacente, caveVisitees, estPasseDeuxFois)
		elif not(estPasseDeuxFois) and caveAdjacente != "start":
			estPasse2Fois = True
			resultat += nombreDeChemins(carte, caveAdjacente, caveVisitees, estPasse2Fois)

	return resultat

memory = []
estPasseDeuxFois = False
print(nombreDeChemins(carte, "start", memory, estPasseDeuxFois))