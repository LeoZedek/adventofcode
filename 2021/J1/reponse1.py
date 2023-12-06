f = open("input")

tab = []

for x in f:
	tab.append(int(x))

f.close()
r = 0
for i in range(1, len(tab)):
	if tab[i - 1] < tab[i]:
		r += 1

print(r)