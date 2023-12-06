## Ce script ne marche pas

f = open('input')

data = list(map(lambda x : x.split('\n')[0], f.readlines()))

f.close()

arborescence = {}
previousesDirectories = {}
previousDir = None
currentDir = None
visitedDirectories = set()

for i, command in enumerate(data):
	list_command = command.split(' ')

	if list_command[0] == "$":
		if list_command[1] == "cd":

			if list_command[2] == ".." and currentDir != "/":
				currentDir = previousesDirectories[currentDir]

			elif list_command[2] != "..":
				previousDir = currentDir
				visitedDirectories.add(previousDir)
				currentDir = list_command[2]
				print(currentDir)
				print(previousDir)
				print("")

				if not(currentDir in arborescence):
					arborescence[currentDir] = []

					if previousDir != None:
						previousesDirectories[currentDir] = previousDir

	else:
		if not(currentDir in visitedDirectories):
			arborescence[currentDir].append(list_command)
print(previousesDirectories)
def calcule_poids(arborescence, directorie):
	poids_total = 0
	#print(directorie)
	#print(arborescence[directorie])
	for file in arborescence[directorie]:

		if file[0] == "dir":
			poids_total += calcule_poids(arborescence, file[1])

		elif file[0] != "..":
			poids_total += int(file[0])


	return poids_total

print(calcule_poids(arborescence, '/'))