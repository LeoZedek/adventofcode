f = open('input')

data = list(map(lambda x : x.split('\n')[0], f.readlines()))

f.close()

def update_score(score, numberCycle, x):

	if numberCycle == 20 or (numberCycle - 20)%40 == 0:
		return score + numberCycle * x

	else:
		return score

score = 0
x = 1


numberCycle = 1
i = 0

while numberCycle <= 240:

	if numberCycle == 1:
		print("#", end='')
	else:

		if abs(((numberCycle % 40) - 1) - x) <= 1:
			print("#", end='')
		else:
			print(".", end='')

		if (numberCycle % 40) == 0:
			print("")

	## Begin of the cycle

	score = update_score(score, numberCycle, x)

	##End of the cycle

	instruction = data[i].split(' ')

	if len(instruction) == 2:
		numberCycle += 1

		if abs(((numberCycle % 40) - 1) - x) <= 1:
			print("#", end='')
		else:
			print(".", end='')

		if (numberCycle % 40) == 0:
			print("")

		score = update_score(score, numberCycle, x)
		x += int(instruction[1])
		numberCycle += 1


	else:
		numberCycle += 1


	i += 1

print("")
print("result 1 :", score)