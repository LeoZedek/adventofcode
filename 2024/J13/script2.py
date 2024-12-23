import re

with open('input') as file:
	data = file.read().splitlines()

r = 0

for i in range(0, len(data), 4):
	Aline = data[i]
	Bline = data[i+1]
	Totalline = data[i+2]

	ax = int(re.search(r'X\+\d+', Aline).group()[2:])
	ay = int(re.search(r'Y\+\d+', Aline).group()[2:])
	bx = int(re.search(r'X\+\d+', Bline).group()[2:])
	by = int(re.search(r'Y\+\d+', Bline).group()[2:])
	totalx = int(re.search(r'X=\d+', Totalline).group()[2:]) + 10000000000000
	totaly = int(re.search(r'Y=\d+', Totalline).group()[2:]) + 10000000000000

	b = (totalx * ay - totaly * ax) / ((bx * ay) - (by * ax))
	a = (totalx - b * bx) / ax

	a = int(a)
	b = int(b)

	if totalx == a * ax + b * bx and totaly == a * ay + b * by:
		r += a * 3 + b

print(r)