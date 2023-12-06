### DATA READING ###

f = open('input')

data = f.readlines()

f.close()

convert = data[0].split('\n')[0]

DataGrille = []

for i in range(2, len(data)):
	DataGrille.append(data[i].split('\n')[0])

class Grille:
	def __init__(self):
		self.grille = {}
		self.NoneValue = False

inputGrille = Grille()

for i in range(len(DataGrille)):
	for j in range(len(DataGrille[i])):
		key = ",".join([str(i), str(j)])
		if DataGrille[i][j] == '#':
			inputGrille.grille[key] = True
		else:
			inputGrille.grille[key] = False

### ALGORITHME ###

def binaireEnNombre(chaine):
	nombre = 0
	for i in range(0, len(chaine)):
		nombre += int(chaine[i]) * 2**(len(chaine) - i - 1)

	return nombre


def calculOutputGrille(inputGrille):
	caseDejaCalculee = []
	outputGrille = Grille()

	for key in inputGrille.grille.keys():
		i, j = key.split(',')
		i, j = int(i), int(j)

		for i2 in range(i - 1, i + 2):
			for j2 in range(j - 1, j + 2):
				key2 = ','.join([str(i2), str(j2)])

				#if not(key2 in caseDejaCalculee):
				if True:
					caseDejaCalculee.append(key2)

					nombreBinaire = ''

					for i3 in range(i2 - 1, i2 + 2):
						for j3 in range(j2 - 1, j2 + 2):
							key3 = ','.join([str(i3), str(j3)])

							if not(key3 in inputGrille.grille.keys()):
								if inputGrille.NoneValue == False:
									nombreBinaire = nombreBinaire + '0'
								else:
									nombreBinaire = nombreBinaire + '1'

							else:
								if inputGrille.grille[key3]:
									nombreBinaire = nombreBinaire + '1'
								else:	
									nombreBinaire = nombreBinaire + '0'

					nombre = binaireEnNombre(nombreBinaire)
					outputGrille.grille[key2] = convert[nombre] == '#'

	if inputGrille.NoneValue == False:
		outputGrille.NoneValue = convert[0] == '#'

	else:
		outputGrille.NoneValue = convert[-1] == '#'

	return outputGrille

for k in range(50):
	print(k)
	inputGrille = calculOutputGrille(inputGrille)

resultat = 0

for value in inputGrille.grille.values():
	if value:
		resultat += 1

print(resultat)
