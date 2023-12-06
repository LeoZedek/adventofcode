with open("input", "r") as file:
	data = file.readlines()

result = 0

for line in data:

	game_name, configuration = line.split(": ")

	game_id = int(game_name.split()[1])

	informations = configuration.split("; ")

	min_red = 0
	min_blue = 0
	min_green = 0

	for info in informations:

		cubes = info.split(", ")

		for cube in cubes:

			number, color = cube.split()
			number = int(number)

			if color == "red":
				if number > min_red:
					min_red = number
			if color == "blue":
				if number > min_blue:
					min_blue = number
			if color == "green":
				if number > min_green:
					min_green = number

	result += min_green * min_blue * min_red

print(result)