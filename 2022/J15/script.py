with open('input') as f:
	data = list(map(lambda x: x.split('\n')[0], f.readlines()))

class Sensor():

	def __init__(self, xSensor, ySensor, xBeacon, yBeacon):

		self.pos = (xSensor, ySensor)
		self.beacon_pos = (xBeacon, yBeacon)

	@property
	def x(self):
		return self.pos[0]

	@property
	def y(self):
		return self.pos[1]
	
	@property
	def x_beacon(self):
		return self.beacon_pos[0]

	@property
	def y_beacon(self):
		return self.beacon_pos[1]
	
	def distance_from_nearest_beacon(self):
		return abs(self.x - self.x_beacon) + abs(self.y - self.y_beacon)

def update(list_range):

	is_update = True

	while is_update:
		is_update = False

		for i in range(len(list_range) - 1):
			if list_range[i + 1][0] <= list_range[i][1]:
				borne_inf = list_range[i][0]
				borne_sup = list_range[i + 1][1]

				list_range.pop(i)
				list_range.pop(i)

				is_update = True

				list_range.insert(i, (borne_inf, borne_sup))
				break

sensors = set()
beacons = set()

for string in data:

	string_list = string.split(' ')
	xSensor = int(string_list[2][2 : -1])
	ySensor = int(string_list[3][2 : -1])

	xBeacon = int(string_list[8][2 : -1])
	yBeacon = int(string_list[9][2 :])

	sensors.add(Sensor(xSensor, ySensor, xBeacon, yBeacon))
	beacons.add((xBeacon, yBeacon))

row = 2000000

no_beacon_positions = set()
range_no_beacon_positions = []

for sensor in sensors:

	distance_beacon = sensor.distance_from_nearest_beacon()
	distance_row_sensor = abs(sensor.y - row)

	if distance_row_sensor <= distance_beacon:

		# for x in range(sensor.x - (distance_beacon - distance_row_sensor), sensor.x + (distance_beacon - distance_row_sensor) + 1 ):
		# 	if not (x, row) in beacons:
		# 		no_beacon_positions.add((x, row))

		borne_inf = sensor.x - (distance_beacon - distance_row_sensor)
		borne_sup = sensor.x + (distance_beacon - distance_row_sensor)

		range_no_beacon_positions.append((borne_inf, borne_sup))

	range_no_beacon_positions.sort(key = lambda x :x[0])

update(range_no_beacon_positions)

print(range_no_beacon_positions[0][1] - range_no_beacon_positions[0][0])

test = [(1, 13), (14, 14), (15, 15), (15, 20)]

update(test)
print(test)