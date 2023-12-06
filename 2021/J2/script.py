f = open('input')
tab = []
for x in f:
	tab.append(x)
	
f.close()
	
for i in range(len(tab)):
	tab[i] = tab[i].split('\n')[0]

for i in range(len(tab)):
	tab[i] = [tab[i].split()[0], tab[i].split()[1]]

aim = 0
profondeur = 0
direction = 0
print(len(tab))
for i in range(len(tab)):
	if tab[i][ 0] == 'forward':
		direction = direction + int(tab[i][1])
		profondeur = profondeur + aim * int(tab[i][1])
	elif tab[i][ 0] == 'down':
		aim = aim + int(tab[i][1])
	else:
		aim = aim - int(tab[i][1])
		
print(profondeur * direction)
