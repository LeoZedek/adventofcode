f = open('input')

data = f.readlines()

f.close()

import numpy as np

for i in range(len(data)):
	data[i] = data[i].split('\n')[0]
	data[i] = list(data[i])

for i in range(len(data)):
	for j in range(len(data[i])):
		data[i][j] = int(data[i][j])
		
sumLowest = 0

def trucR(tab, i, j, memo):
	key = ",".join([str(i), str(j)])
	
	if key in memo:
		return 0
	
	memo.append(key)
	
	s = 1
	
	if i > 0:
		if data[i - 1][j] >	 data[i][j] and data[i - 1][j] != 9:
			s += trucR(tab, i - 1, j, memo)
		
	if i < len(tab) - 1:
		if data[i + 1][j] > data[i][j] and data[i + 1][j] != 9:
			s += trucR(tab, i + 1, j, memo)
	
	if j > 0:
		if data[i][j - 1] > data[i][j] and data[i][j - 1] != 9:
			s += trucR(tab, i, j - 1, memo)
	
	if j < len(tab	[i]) - 1:
		if data[i][j + 1] > data[i][j] and data[i][j + 1] != 9:
			s += trucR(tab, i, j + 1, memo)

	
	return s
	
taillesBassins = []
for i in range(len(data)):
	for j in range(len(data[i])):
		isLowest = True
		
		if i > 0:
			if data[i - 1][j] <= data[i][j]:
				isLowest = False
		
		if i < len(data) - 1:
			if data[i + 1][j] <= data[i][j]:
				isLowest = False
		
		if j > 0:
			if data[i][j - 1] <= data[i][j]:
				isLowest = False
		
		if j < len(data[i]) - 1:
			if data[i][j + 1] <= data[i][j]:
				isLowest = False
				
		if isLowest:
			sumLowest += data[i][j] + 1
			memo = []
			taillesBassins.append(trucR(data, i, j, memo))
		
lesPlusGrands = []

print(taillesBassins)

for i in range(3):
	lesPlusGrands.append(np.max(taillesBassins))
	taillesBassins.remove(np.max(taillesBassins))
	



print(np.prod(lesPlusGrands))
			
