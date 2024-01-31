HEXAVALUE = {
	"0" : 0,
	"1" : 1,
	"2" : 2,
	"3" : 3,
	"4" : 4,
	"5" : 5,
	"6" : 6,
	"7" : 7,
	"8" : 8,
	"9" : 9,
	"a" : 10,
	"b" : 11,
	"c" : 12,
	"d" : 13,
	"e" : 14,
	"f" : 15,
}

RIGTH = 0
DOWN = 1
LEFT = 2
UP = 3

directions = {
	"0": RIGTH,
	"1": DOWN,
	"2": LEFT,
	"3": UP
}

directions_letter = {
	"R": RIGTH,
	"D": DOWN,
	"L": LEFT,
	"U": UP
}

deltas = {
	RIGTH: (0, 1),
	LEFT: (0, -1),
	UP: (-1, 0),
	DOWN: (1, 0)
}

def hexa_to_dec(hexa):

	result = 0

	for i in range(len(hexa)):
		result += 16**(len(hexa) - (i + 1)) * HEXAVALUE[hexa[i]]

	return result

with open("input", "r") as file:
	data = file.readlines()

points = [(0, 0)]
perimeter = 0

for i in range(len(data)):

	full_hexa = data[i].split()[2][2:-1]
	
	direction = directions[full_hexa[-1]]
	distance = hexa_to_dec(full_hexa[:-1])

	perimeter += distance

	delta = deltas[direction]
	previous_point = points[-1]

	next_point = tuple((previous_point[i] + delta[i] * distance for i in range(len(previous_point))))
	points.append(next_point)

inside = 0

for i in range(len(points) - 1):

	inside += points[i][1] * points[i+1][0] - points[i][0] * points[i+1][1]

print(abs(inside)//2 + 3 + (perimeter - len(data)) // 2 + (len(data) - 4) // 2)