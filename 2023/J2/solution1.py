with open("input", "r") as file:
	data = file.readlines()

result = 0

for line in data:
	possible = True

	game_name, configuration = line.split(": ")

	game_id = int(game_name.split()[1])

	informations = configuration.split("; ")

	for info in informations:

		cubes = info.split(", ")

		for cube in cubes:

			number, color = cube.split()
			number = int(number)

			if color == "blue" and number > 14:
				possible = False

			if color == "red" and number > 12:
				possible = False

			if color == "green" and number > 13:
				possible = False

	if possible:
		result += game_id

print(result)