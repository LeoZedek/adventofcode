f = open("input")

data = f.readlines()

f.close()

for i in range(len(data)):
	data[i] = data[i].split('\n')[0]

calories = []

tempCalorie = 0

for calorie in data:
	if calorie != "":
		tempCalorie += int(calorie)
	else:
		calories.append(tempCalorie)
		tempCalorie = 0


calories.sort()


print(calories[-1] + calories[-2] + calories[-3])