f = open('input')

data = f.readlines();

f.close()

for i in range(len(data)):	
	data[i] = data[i].split('\n')[0]
	
print(data[20])

def obtenirElt(pile):
	return(pile[-1])
	
def depiler(pile):
	pile.pop()
	
def empiler(pile, elt):
	pile.append(elt);

def estVide(pile):
	return len(pile) == 0

dicoScore = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
	
def score(lettre):
	return dicoScore[lettre]
	
dicoReverse = {')' : '(', ']' : '[', '}' : '{', '>' : '<'}
def reverse(lettre):
	return dicoReverse[lettre]

dicoScore2 = {'(' : 1, '[' : 2, '{' : 3, '<' : 4}

debutChunk = ['(', '<', '[', '{']
finChunk = [')', '>', ']', '}']

r = 0

resultats = []

for k in range(len(data)):
	pile = []
	continuer = True
	i = 0
	while continuer and i < len(data[k]):
		lettre = data[k][i]
		
		if lettre in debutChunk:
			empiler(pile, lettre)
		
		if lettre in finChunk:
			if len(pile) == 0:
				r += score(lettre)
				continuer = False
			
			elif reverse(lettre) != obtenirElt(pile):
				r += score(lettre)
				continuer = False
				
			else:
				depiler(pile)
				
		i += 1
	
	rTemp = 0
	
	if not(estVide(pile)) and continuer:
		while not(estVide(pile)):
			rTemp = rTemp * 5
			rTemp += dicoScore2[obtenirElt(pile)]
			depiler(pile)
		
		resultats.append(rTemp)

resultats = sorted(resultats)

indiceMoitie = len(resultats) // 2

print(resultats[indiceMoitie])

















		
