f = open("input")

data = f.readlines()

f.close()

for i in range(len(data)):

	line = data[i]

	data[i] = line.split('\n')[0].split(' ')

win = {
	"A" : "Y",
	"B" : "Z",
	"C" : "X"
}

lose = {
	"A" : "Z",
	"B" : "X",
	"C" : "Y"
}

score = {
	"X" : 1,
	"Y" : 2,
	"Z" : 3
}

resultat = 0

for jeu in data:

	if win[jeu[0]] == jeu[1]:
		resultat += 6

	elif lose[jeu[0]] != jeu[1]:
		resultat += 3

	resultat += score[jeu[1]]

print(resultat)
