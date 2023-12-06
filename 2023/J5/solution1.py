# with open("input", "r") as file:
# 	data = file.readlines()

# seeds = list(map(int, data[0].split(": ")[1].split()))

# i = 1

# while data[i] != "seed-to-soil map:\n":
# 	i += 1

# # jump to the mapped value
# i += 1

# seed_to_soil_map = []

# while data[i] != "\n":

# 	seed_to_soil_map.append(list(map(int, data[i].split())))

# 	i += 1

# i += 2

# soil_to_fertilizer_map = []

# while data[i] != "\n":

# 	soil_to_fertilizer_map.append(list(map(int, data[i].split())))

# 	i += 1

# i += 2

# fertilizer_to_water_map = []

# while data[i] != "\n":

# 	fertilizer_to_water_map.append(list(map(int, data[i].split())))

# 	i += 1

# i += 2

# water_to_light_map = []

# while data[i] != "\n":

# 	water_to_light_map.append(list(map(int, data[i].split())))

# 	i += 1

# i += 2

# ligth_to_temp_map = []

# while data[i] != "\n":

# 	ligth_to_temp_map.append(list(map(int, data[i].split())))

# 	i += 1

# i += 2

# temp_to_hum_map = []

# while data[i] != "\n":

# 	temp_to_hum_map.append(list(map(int, data[i].split())))

# 	i += 1

# i += 2

# hum_to_location_map = []

# while i < len(data) and data[i] != "\n":

# 	hum_to_location_map.append(list(map(int, data[i].split())))

# 	i += 1

# i += 2

# min_location = -1
# min_seed = -1
# print(seed_to_soil_map)
# for seed in seeds:

# 	soil = -1
# 	print("seed :", seed)
# 	for mapped_value in seed_to_soil_map:

# 		seed_value_range = mapped_value[1]
# 		length = mapped_value[2]

# 		if seed_value_range <= seed and seed < seed_value_range + length:
# 			soil = mapped_value[0] + seed - seed_value_range

# 	if soil == -1:
# 		soil = seed

# 	fertilizer = -1
# 	print("soil :", soil)
# 	for mapped_value in soil_to_fertilizer_map:

# 		soil_value_range = mapped_value[1]
# 		length = mapped_value[2]

# 		if soil_value_range <= soil and soil < soil_value_range + length:
# 			fertilizer = mapped_value[0] + soil - soil_value_range

# 	if fertilizer == -1:
# 		fertilizer = soil

# 	water = -1
# 	print("fert :", fertilizer )
# 	for mapped_value in fertilizer_to_water_map:

# 		fertilizer_value_range = mapped_value[1]
# 		length = mapped_value[2]

# 		if fertilizer_value_range <= fertilizer and fertilizer < fertilizer_value_range + length:
# 			water = mapped_value[0] + fertilizer - fertilizer_value_range

# 	if water == -1:
# 		water = fertilizer

# 	light = -1
# 	print("water :", water)
# 	for mapped_value in water_to_light_map:

# 		water_value_range = mapped_value[1]
# 		length = mapped_value[2]

# 		if water_value_range <= water and water < water_value_range + length:
# 			light = mapped_value[0] + water - water_value_range

# 	if light == -1:
# 		light = water

# 	temp = -1
# 	print("light :", light)
# 	for mapped_value in ligth_to_temp_map:

# 		ligth_value_range = mapped_value[1]
# 		length = mapped_value[2]

# 		if ligth_value_range <= light and light < ligth_value_range + length:
# 			temp = mapped_value[0] + light - ligth_value_range

# 	if temp == -1:
# 		temp = light

# 	hum = -1
# 	print("temp :", temp)
# 	for mapped_value in temp_to_hum_map:

# 		temp_value_range = mapped_value[1]
# 		length = mapped_value[2]

# 		if temp_value_range <= temp and temp < temp_value_range + length:
# 			hum = mapped_value[0] + temp - temp_value_range

# 	if hum == -1:
# 		hum = temp

# 	location = -1
# 	print("hum : ", hum)
# 	for mapped_value in hum_to_location_map:

# 		hum_value_range = mapped_value[1]
# 		length = mapped_value[2]

# 		if hum_value_range <= hum and hum < hum_value_range + length:
# 			location = mapped_value[0] + hum - hum_value_range

# 	if location == -1:
# 		location = hum
# 	print("location :", location)
# 	if min_location == -1 or location < min_location:
# 		min_location = location
# 		min_seed = seed

# print(min_location)

#####

with open("input", "r") as file:
	data = file.readlines()

seeds = list(map(int, data[0].split(": ")[1].split()))

i = 3

mapped_values = []

while i < len(data):
	
	mapped_value = []

	while i < len(data) and data[i] != "\n":
		mapped_value.append(list(map(int, data[i].split())))
		i += 1

	mapped_values.append(mapped_value)

	i += 2

min_location = -1

for seed in seeds:
	value_source = seed
	value_destination = -1

	i = 0

	while i < len(mapped_values):

		mapped_source_to_dest = mapped_values[i]

		value_destination = -1

		for mapped_value in mapped_source_to_dest:

			source_value_range = mapped_value[1]
			length = mapped_value[2]

			if source_value_range <= value_source and value_source < source_value_range + length:
				value_destination = mapped_value[0] + value_source - source_value_range

			if value_destination == -1:
				value_destination = value_source

		i += 1

		value_source = value_destination

	if min_location == -1 or value_destination < min_location:
		min_location = value_destination

print(min_location)