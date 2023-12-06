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

def calculerVictoire(joueur1, joueur2, etape, memory):

	score1 = joueur1.score ## Pour que se soit seulement en entrée et pas en entrée
	score2 = joueur2.score
	joueur1 = Player(joueur1.position)
	joueur2 = Player(joueur2.position)

	joueur1.score = score1
	joueur2.score = score2

	if joueur1.score >= 21:
		return 1, 0
	elif joueur2.score >= 21:
		return 0, 1
	
	else:

		key = ",".join([str(joueur1.position), str(joueur2.position), str(joueur1.score), str(joueur2.score), str(etape)])

		if key in memory.keys():
			return memory[key]

		victoire1, victoire2 = 0, 0
	
		if etape == 1 or etape == 2:

			for i in range(3):

				joueur1.position = (joueur1.position + 1) % 10

				temp1, temp2 = calculerVictoire(joueur1, joueur2, etape + 1, memory)

				victoire1 += temp1
				victoire2 += temp2
			
			memory[key] = victoire1, victoire2

			return memory[key]

		elif etape == 3:
			memScore = joueur1.score

			for i in range(3):

				joueur1.position = (joueur1.position + 1) % 10

				joueur1.score = memScore + joueur1.position + 1

				if joueur1.score >= 21:
					victoire1 += 1
				else:
					temp1, temp2 = calculerVictoire(joueur1, joueur2, etape + 1, memory)
					victoire1 += temp1
					victoire2 += temp2

			memory[key] = victoire1, victoire2

			return memory[key]

		elif etape == 4 or etape == 5:
			for i in range(3):

				joueur2.position = (joueur2.position + 1) % 10

				temp1, temp2 = calculerVictoire(joueur1, joueur2, etape + 1, memory)
				victoire1 += temp1
				victoire2 += temp2

			memory[key] = victoire1, victoire2

			return memory[key]

		elif etape == 6:

			memScore = joueur2.score

			for i in range(3):

				joueur2.position = (joueur2.position + 1) % 10

				joueur2.score = memScore + joueur2.position + 1

				if joueur2.score >= 21:
					victoire2 += 1
				else:
					temp1, temp2 = calculerVictoire(joueur1, joueur2, 1, memory)
					victoire1 += temp1
					victoire2 += temp2

			memory[key] = victoire1, victoire2

			return memory[key]


memory = {}

victoire1, victoire2 = calculerVictoire(joueur1, joueur2, 1, memory)

print(np.max([victoire1,victoire2]))