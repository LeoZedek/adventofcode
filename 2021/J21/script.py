### Data readings ###

f = open('input')
data = f.readlines()
f.close()

class Player:
	def __init__(self, positionInitial):
		self.position = positionInitial
		self.score = 0

joueur1 = Player(int(data[0][-2]) - 1)
joueur2 = Player(int(data[1][-2]) - 1)

###Algorithme###
import numpy as np

def tirerDe(nbTirage):
	return nbTirage % 100 + 1

partiFinis = False
nbTirage = 0

while not(partiFinis):
	
	memDe = []
	for i in range(3):
		memDe.append(tirerDe(nbTirage))
		nbTirage += 1

	joueur1.position = (joueur1.position + np.sum(memDe)) % 10
	joueur1.score += joueur1.position + 1
	print(joueur1.score)

	partiFinis = joueur1.score >= 1000

	if not(partiFinis):
		memDe = []
		for i in range(3):
			memDe.append(tirerDe(nbTirage))
			nbTirage += 1

		joueur2.position = (joueur2.position + np.sum(memDe)) % 10
		joueur2.score += joueur2.position + 1
		print(joueur2.score)

	partiFinis = joueur1.score >= 1000 or joueur2.score >= 1000

scoreMin = np.min([joueur1.score, joueur2.score])

print(scoreMin * nbTirage)