f = open('input')

data = f.readline()

data = data.split('\n')[0]

xRange, yRange = data.split(', ')

xRange = xRange.split('x=')[1]
xRange = xRange.split('..')

yRange = yRange.split('y=')[1]
yRange = yRange.split('..')

yRange[0], yRange[1] = int(yRange[0]), int(yRange[1])
xRange[0], xRange[1] = int(xRange[0]), int(xRange[1])

def valeurY(x, y, xRange, yRange):
	yMax = 0
	
	continuer = True
	valide = False
	
	xProbe = 0
	yProbe = 0
	
	while continuer:
		
		xProbe += x
		yProbe += y
		
		if yProbe> yMax:
			yMax = yProbe
		
		continuer = (xProbe <= xRange[1] and yProbe >= yRange[0]) and not(xProbe >= xRange[0] and xProbe <= xRange[1] and yProbe >= yRange[0] and yProbe <= yRange[1]);
		if (xProbe >= xRange[0] and xProbe <= xRange[1] and yProbe >= yRange[0] and yProbe <= yRange[1]):
			valide = True;
			
		if x > 0:
			x += -1
		elif x < 0:
			x += 1
			
		y += -1	

		
	return yMax, valide
	
x = 0;
xTrouve = False

while not(xTrouve):
	x += 1
	distance = 0
	for i in range(x + 1):
		distance += i
		
	xTrouve = (distance <= xRange[1] and distance >= xRange[0]) or x == xRange[0]
	
y = - yRange[0] - 1

r = 0

for x2 in range(1, xRange[1] + 1):
	for y2 in range(yRange[0], y + 1):
		_, atteintTarget = valeurY(x2, y2, xRange, yRange)
		
		if atteintTarget:
			r += 1	
		
print(valeurY(x, y, xRange, yRange))
print(r)



























