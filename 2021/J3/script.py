f = open("input")

tab = []

for x in f:
	tab.append(str(x))
	
f.close()
	
gamma = []
for k in range(len(tab[0]) - 1):
	nb1 = 0
	nb0 = 0
	for i in range(len(tab)):
		if tab[i][k] == '1':
			nb1 = nb1 + 1
		else:
			nb0 = nb0 + 1
	
	if nb1 > nb0:
		gamma.append(1)
	else:
		gamma.append(0)

print(gamma)

epsilon = []

for i in range(len(gamma)):
	
	if gamma[i] == 1:
		epsilon.append(0)
	else:
		epsilon.append(1)

print(epsilon)

resultEpsilon = 0
resultGamma = 0

for i in range(len(epsilon)):
	resultEpsilon = resultEpsilon + epsilon[i] * 2**(11 - i)
	resultGamma = resultGamma + gamma[i] * 2**(11 - i)
	
print(resultEpsilon)

print(resultEpsilon * resultGamma);

