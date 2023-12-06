f = open('input')

data = f.readline()

f.close()

data = data.split('\n')[0]

import numpy as np

def decEnBinaire(n):
	resultat = ''
	
	while n != 0:
		r = n % 2
		n = n // 2
		resultat = str(r) + resultat
		
	while len(resultat) < 4:
		resultat = '0' + resultat
		
	return resultat
	

chiffres = "0123456789ABCDEF"
hexaEnBinaire = {}

for i in range(len(chiffres)):
	hexaEnBinaire[chiffres[i]] = i


def binaireEnNombre(nbEnBinaire):
	r = 0
	taille = len(nbEnBinaire)
	
	for i in range(taille):
		r += int(nbEnBinaire[i]) *  2**(taille - i - 1)
	
	return r

def traiterUnPaquet(paquet, debut):
	
	i = debut
	
	sumVersion = 0
	
	version = int(paquet[i]) * 4 + int(paquet[i + 1]) * 2 + int(paquet[i + 2])
	
	sumVersion += version
	i += 3
	
	ID = int(paquet[i]) * 4 + int(paquet[i + 1]) * 2 + int(paquet[i + 2])
	i += 3
	
	sumNombre = 0
	
	if ID == 4:
		nombreEnBinaire = ''
		continuer = True
		while continuer:
			continuer = int(paquet[i])
			
			for k in range(i + 1, i + 5):
				nombreEnBinaire = nombreEnBinaire + paquet[k]
			
			i += 5
		nombre = binaireEnNombre(nombreEnBinaire)
		return sumVersion, nombre, i
		
	
	else:
		
		if paquet[i] == '0':
			
			i += 1
			tailleBinaire = ''
			
			for k in range(i, i + 15):
				tailleBinaire = tailleBinaire + paquet[k]
				
			taille = binaireEnNombre(tailleBinaire)
			i += 15
			
			iFreeze = i
			
			nombres = []
			
			while (i < iFreeze + taille):
				tempVersion, tempNombre, i = traiterUnPaquet(paquet, i)
				sumVersion += tempVersion
				nombres.append(tempNombre)
				
			
		elif paquet[i] == '1':
			
			i += 1
			nbSsPaquetBinaire = ''
			
			for k in range(i, i + 11):
				nbSsPaquetBinaire = nbSsPaquetBinaire + paquet[k]
			
			nbSsPaquet = binaireEnNombre(nbSsPaquetBinaire)
			i += 11
			
			nombres = []
			
			for step in range(nbSsPaquet):
				tempVersion, tempNombre, i = traiterUnPaquet(paquet, i)
				sumVersion += tempVersion
				nombres.append(tempNombre)
				
		if ID == 0:
			nombre = np.sum(nombres)

		elif ID == 1:		
			nombre = np.prod(nombres)
			
		elif ID == 2:
			nombre = np.amin(nombres)
			
		elif ID == 3:
			nombre = np.amax(nombres)

		elif ID == 5:
			nombre = int(nombres[0] > nombres[1])
			
		elif ID == 6:
			nombre = int(nombres[0] < nombres[1])
			
		elif ID == 7:
			nombre = int(nombres[0] == nombres[1])
			
		return sumVersion, nombre, i
	
dataBinaire = ''



for i in range(len(data)):
	dataBinaire += decEnBinaire(hexaEnBinaire[data[i]])


print(traiterUnPaquet(dataBinaire, 0))



