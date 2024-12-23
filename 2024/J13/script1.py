import re
from sympy import symbols, Eq, solve

with open('input') as file:
	data = file.read().splitlines()

r = 0

for i in range(0, len(data), 4):
	Aline = data[i]
	Bline = data[i+1]
	Totalline = data[i+2]

	ax = int(re.search('X\+\d+', Aline).group()[2:])
	ay = int(re.search('Y\+\d+', Aline).group()[2:])
	bx = int(re.search('X\+\d+', Bline).group()[2:])
	by = int(re.search('Y\+\d+', Bline).group()[2:])
	totalx = int(re.search('X=\d+', Totalline).group()[2:])
	totaly = int(re.search('Y=\d+', Totalline).group()[2:])

	a, b = symbols('a b')

	eqX = Eq(ax*a + bx*b - totalx)
	eqY = Eq(ay*a + by*b - totaly)

	solution = solve((eqX,eqY), (a, b))
	print(solution[a])
	if solution:
		r += solution[a] * 3 + solution[b]

print(r)