f = open('input')

numbers = f.readline().split('\n')[0]
numbers = numbers.split(',')

f.readline()

tab = f.readlines()

f.close()

grilles = []
grille = []


for x in tab:
	if x != '\n':
		grille.append(x.split('\n')[0].split())
	else:
		grilles.append(grille.copy())
		grille = []

grilles.append(grille)

nombreTire = []

n = len(grilles[0])
p = len(grilles[0][0])

def estLigneGagnante(grille, y):
	resultat = True
	j = 0
	while (resultat and j < p):
		if not(grille[y][j] in nombreTire):
			resultat = False
		
		j = j + 1
	
	return resultat

def estColonneGagnante(grille, x):
	resultat = True
	i = 0
	while (resultat == True and i < n):
		if not(grille[i][x] in nombreTire):
			resultat = False
		
		i = i + 1
	
	return resultat

def estGrilleGagnante(grille):
	resultat = False
	
	for i in range(n):
		if estLigneGagnante(grille, i):
			resultat = True
	
	for j in range(p):
		if estColonneGagnante(grille, j):
			resultat = True
			
	return resultat

partieFini = False
indice = 0

while not(len(grilles) == 0):
	nombreTire.append(numbers[indice])
	
	grillesGagnantes = []
	
	for i in range(len(grilles)):
		if estGrilleGagnante(grilles[i]):
			grillesGagnantes.append(grilles[i])
			
	for x in grillesGagnantes:
		grilles.remove(x)
	
	indice = indice + 1
	
	if len(grilles) == 1:
		grilleP = grilles[0]
	



resultat = 0

for i in range(n):
	for j in range(p):
		if not(grilleP[i][j] in nombreTire):
			resultat = resultat + int(grilleP[i][j])

print(resultat * int(nombreTire[-1]))

