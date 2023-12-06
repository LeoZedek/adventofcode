f = open("input")

tab = []

for x in f:
	tab.append(str(x))

f.close();

oxygen = []

for x in tab:
	oxygen.append(x)

k = 0

while (len(oxygen) != 1 and k < len(oxygen[0])):

	nb1 = 0
	nb0 = 0
	for i in range(len(oxygen)):
		if oxygen[i][k] == '1':
			nb1 = nb1 + 1
		else:
			nb0 = nb0 + 1
	result = []
	
	if nb1 >= nb0:
		for i in range(len(oxygen)):
			if oxygen[i][k] == '1':
				result.append(oxygen[i])
		
	else:
		for i in range(len(oxygen)):
			if oxygen[i][k] == '0':
				result.append(oxygen[i])
	
	oxygen = []
	for x in result:
		oxygen.append(x)
		
	k = k + 1;
	

co2 = []

for x in tab:
	co2.append(x)

k = 0

while (len(co2) != 1 and k < len(co2[0])):

	nb1 = 0
	nb0 = 0
	for i in range(len(co2)):
		if co2[i][k] == '1':
			nb1 = nb1 + 1
		else:
			nb0 = nb0 + 1
	result = []
	
	if nb1 < nb0:
		for i in range(len(co2)):
			if co2[i][k] == '1':
				result.append(co2[i])
		
	else:
		for i in range(len(co2)):
			if co2[i][k] == '0':
				result.append(co2[i])
	
	co2 = []
	for x in result:
		co2.append(x)
		
	k = k + 1;

print(oxygen)
print(co2)
Roxygen = 0
Rco2 = 0

for i in range(len(oxygen[0]) - 1):
	Roxygen = Roxygen + int(oxygen[0][i]) * 2**(11 - i)
	Rco2 = Rco2 + int(co2[0][i]) * 2**(11 - i)
	
print(Roxygen * Rco2)














