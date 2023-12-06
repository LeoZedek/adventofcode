f = open('input')

continuer = True
points = {}

while continuer:
	data = f.readline()
	
	if data != '\n':

		key = ','.join(data.split('\n')[0].split(','))
		points[key] = True
		
	else:
		continuer = False
		
plits = f.readlines()

for i in range(len(plits)):
	plits[i] = plits[i].split('\n')[0].split(' ')[2].split('=')
	plits[i][1] = int(plits[i][1])

f.close()

for i in range(len(plits)):

	newKeys = []

	for key in points.keys():
		xPoints, yPoints = key.split(',')
		xPoints = int(xPoints)
		yPoints = int(yPoints)
		
		if plits[i][0] == 'y':
			yPlit = plits[i][1]
			if yPoints > yPlit and points[key]:
				newYPoints = yPlit - (yPoints - yPlit)
				points[key] = False
				newKey = ','.join([str(xPoints), str(newYPoints)])
				newKeys.append(newKey)
		else:
			xPlit = plits[i][1]
			if xPoints > xPlit and points[key]:
				newXPoints = xPlit - (xPoints - xPlit)
				points[key] = False
				newKey = ','.join([str(newXPoints), str(yPoints)])
				newKeys.append(newKey)
				
	for key in newKeys:
		points[key] = True
			
r = 0
x = []
y = []
xMax = 0
yMax = 0

for key, value in points.items():
	if value:
		r += 1
		x = int(key.split(',')[0])
		y = int(key.split(',')[1])
		if x > xMax:
			xMax = x
			
		if y > yMax:
			yMax = y
			
for j in range(yMax + 1):
	for i in range(xMax + 1):
		key = ",".join([str(i), str(j)])
		if key in points.keys():
			if points[key]:
				print('#', end = '')
			else:
				print('.', end = '')
			
		else:
			print('.', end = '')
		
	print('')



print(r)
