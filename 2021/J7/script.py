f = open('input')

data = f.readlines()[0].split('\n')[0].split(',')

f.close()

for i in range(len(data)):
	data[i] = int(data[i])
	
	
fuelUse = {}

for i in range(max(data) + 1):
	r = 0
	for k in range(i):
		r += k + 1
	fuelUse[i] = r
	

resultat = 0	
for i in range(len(data)):
	resultat += fuelUse[data[i]]

for k in range(max(data) + 1):
	temp = 0
	for i in range(len(data)):
		if data[i] > k:
			temp += fuelUse[data[i] - k]
		else:
			temp += fuelUse[k - data[i]]
			
	
	if temp < resultat:
		resultat = temp
		
		

print(resultat)
