f = open('input')

data = f.readlines()

f.close()
chiffres = []

for i in range(len(data)):
	chiffres.append(data[i].split('\n')[0].split(' | ')[0].split(' '))
	data[i] = data[i].split('\n')[0].split(' | ')[1].split(' ')


lettres = 'abcdefg'
r = 0

for i in range(len(data)):
	for x in data[i]:
		if len(x) == 7 or len(x) == 4 or len(x) == 2 or len(x) == 3:
			r += 1
			

dicoTrouve = {1 : '', 2 : '', 3 : '', 4 : '', 5 : '', 6 : '', 7 : '', 8 : '', 9 : ''}
dico = {}
for char in 'abcdefg':
	dico[char] = list('abcdefg');

print(dico)

## Debut facile

def intersection(l1, l2):
	
	print(l1)
	l = l1.copy()
	for elt in l1:
		if not(elt in l2):
			l.remove(elt)
			
	return ''.join(l)

for entree in chiffres[0]:

	entree = list(entree)
	
	print(entree)
	if len(entree) == 2:
		dico['c'] = intersection(dico['c'], entree)
		dico['f'] = intersection(dico['f'], entree)
		dicoTrouve[1] = "".join(entree)
		
	if len(entree) == 3:
		dico['a'] = intersection(dico['a'], entree)
		dico['c'] = intersection(dico['c'], entree)
		dico['f'] = intersection(dico['f'], entree)
		dicoTrouve[7] = "".join(entree)
		
	if len(entree) == 4:
		dico['b'] = intersection(dico['b'], entree)
		dico['c'] = intersection(dico['c'], entree)
		dico['d'] = intersection(dico['d'], entree)
		dico['f'] = intersection(dico['f'], entree)
		dicoTrouve[4] = "".join(entree)
	
	if len(entree) == 7:
		 
		dico['a'] = intersection(dico['a'], entree)
		dico['b'] = intersection(dico['b'], entree)
		dico['c'] = intersection(dico['c'], entree)
		dico['d'] = intersection(dico['d'], entree)
		dico['e'] = intersection(dico['e'], entree)
		dico['f'] = intersection(dico['f'], entree)
		dico['g'] = intersection(dico['g'], entree)
		dicoTrouve[8] = "".join(entree)

print(dico)
		
		
		
		
		
		
		
		
