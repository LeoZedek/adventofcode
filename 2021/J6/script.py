f = open('input')

tab = f.readlines()[0].split()[0].split(',')

f.close()

for i in range(len(tab)):
	tab[i] = int(tab[i])
	
poissons = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0}

for i in range(len(tab)):
	poissons[tab[i]] += 1

for k in range(256):
	temp = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0}
	for i in range(8):
		temp[i] = poissons[i + 1]
	
	temp[8] += poissons[0]
	temp[6] += poissons[0]
	
	poissons = temp.copy()
	
resultat = 0

for value in poissons.values():
	resultat += value
	
print(resultat)
