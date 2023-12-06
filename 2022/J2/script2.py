f = open("input")

data = f.readlines()

f.close()

for i in range(len(data)):

	line = data[i]

	data[i] = line.split('\n')[0].split(' ')

win = {
	"A" : 2,
	"B" : 3,
	"C" : 1
}

lose = {
	"A" : 3,
	"B" : 1,
	"C" : 2
}

draw = {
	"A" : 1,
	"B" : 2,
	"C" : 3
}

score = {
	"X" : 0,
	"Y" : 3,
	"Z" : 6
}

resultat = 0

for jeu in data:

	resultat += score[jeu[1]]

	if jeu[1] == "X":
		resultat += lose[jeu[0]]

	elif jeu[1] == "Y":
		resultat += draw[jeu[0]]

	else:
		resultat += win[jeu[0]]

print(resultat)
