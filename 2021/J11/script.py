f = open('input')

data = f.readlines()

f.close()

for i in range(len(data)):
	data[i] = data[i].split('\n')[0]
	data[i] = list(data[i])
	
	for k in range(len(data[i])):
		data[i][k] = int(data[i][k])
		
	
aFlashe = {}

def initAFlash():

	for i in range(len(data)):
		for j in range(len(data[i])):
			key = ','.join([str(i), str(j)]);
			aFlashe[key] = False

initAFlash()

def max(a, b):
	if a > b:
		return a
	else:
		return b
		
def min(a, b):
	if a < b:
		return a
	else:
		return b
		
resultat = 0

def incrementeOctopus(i, j):
	r = 0
	
	key = ','.join([str(i), str(j)])
	if not(aFlashe[key]):
		if data[i][j] < 9:
			data[i][j] += 1
			
		else:
			data[i][j] = 0
			
			aFlashe[key] = True
			r += 1

			for i2 in range(max(0, i - 1), min(9 + 1, i + 1 + 1)):
				for j2 in range(max(0, i - 1), min(9 + 1, i + 1 + 1)):
					r += incrementeOctopus(i2, j2)
	return r
	

steps = 0
FlashEnMemeTmp = False
while not(FlashEnMemeTmp):
	
	for i in range(len(data)):
		for j in range(len(data[i])):
			data[i][j] += 1
	
	continuer = True
	while continuer:
		continuer = False
		
		for i in range(len(data)):
			for j in range(len(data[i])):
			
				key = ','.join([str(i), str(j)])
			
				if data[i][j] > 9 and not(aFlashe[key]):
					continuer = True
					aFlashe[key] = True
					resultat += 1
					
					for i2 in range(max(0, i - 1), min(9 + 1, i + 1 + 1)):
						for j2 in range(max(0, j - 1), min(9 + 1, j + 1 + 1)):
							key = ','.join([str(i2), str(j2)])
							if not(aFlashe[key]):
								data[i2][j2] += 1
	
	for i in range(len(data)):
		for j in range(len(data[i])):
			key = ','.join([str(i), str(j)])
			
			if aFlashe[key]:
				data[i][j] = 0
				
	FlashEnMemeTmp = True
	
	for i in range(len(data)):
			for j in range(len(data[i])):
			
				key = ','.join([str(i), str(j)])
				
				if not(aFlashe[key]):
					 FlashEnMemeTmp = False
	
	initAFlash()
	
	steps += 1
	
print(steps)
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
