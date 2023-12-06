f = open('input')

data = f.readlines();

f.close()

for i in range(len(data)):
	data[i] = data[i].split('\n')[0]
	data[i] = data[i].split(' -> ')
	data[i][0] = data[i][0].split(',')
	data[i][1] = data[i][1].split(',')
	
	data[i][0][0] = int(data[i][0][0])
	data[i][0][1] = int(data[i][0][1])
	data[i][1][0] = int(data[i][1][0])
	data[i][1][1] = int(data[i][1][1])
	
grille = {}
	
for i in range(len(data)):
	x1 = data[i][0][0]
	x2 = data[i][1][0]
	y1 = data[i][0][1]
	y2 = data[i][1][1]
	
	if x1 == x2:
	
		if y2 > y1:
			for k in range(y1, y2 + 1):
			
				key = ','.join([str(x1), str(k)])
				if (key in grille):
					grille[key] = grille[key] + 1
				else:
					grille[key] = 1
				
		else:
			for k in range(y2, y1 + 1):
			
				key = ','.join([str(x1), str(k)])
				if (key in grille):
					grille[key] = grille[key] + 1
				else:
					grille[key] = 1
		
	elif y1 == y2:
		
		if x2 > x1:
			for k in range(x1, x2 + 1):
				
				key = ','.join([str(k), str(y1)])
				if (key in grille):
					grille[key] = grille[key] + 1
				else:
					grille[key] = 1
				
		else:
			for k in range(x2, x1 + 1):
			
				key = ','.join([str(k), str(y1)])
				if (key in grille):
					grille[key] = grille[key] + 1
				else:
					grille[key] = 1
	
	# La partie avec les diagonales en dessous
	
	elif x2 > x1:
		for k in range(x1, x2 + 1):
				
				if y2 > y1:
					key = ','.join([str(k), str(y1 + (k - x1))])
				else:
					key = ','.join([str(k), str(y1 - (k - x1))])
				
				
				if (key in grille):
					grille[key] = grille[key] + 1
				else:
					grille[key] = 1 
	
	elif x2 < x1:
		for k in range(x2, x1 + 1):
				
				if y2 > y1:
					key = ','.join([str(k), str(y2 - (k - x2))])
				else:
					key = ','.join([str(k), str(y2 + (k - x2))])
				
				
				if (key in grille):
					grille[key] = grille[key] + 1
				else:
					grille[key] = 1 
	
					
resultat = 0
for val in grille.values():
	if val > 1:
		resultat = resultat + 1

print(resultat)
						
























