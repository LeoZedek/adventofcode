f = open('input')

data = f.readlines()

f.close()

nbStack = len(data[0]) // 4

stacks = []

for i in range(nbStack):
	stacks.append([])

indData = 0

while (data[indData] != "\n"):
	for i in range(nbStack):

		obj = data[indData][(i * 4 + 1)]
		if obj != ' ':

			stacks[i].insert(0, obj)

	indData += 1

indData += 1

while (indData < len(data)):
	line = data[indData]

	_, nbMove, _, origine_stack, _, destination_stack = line.split('\n')[0].split(' ')

	nbMove = int(nbMove)
	origine_stack = int(origine_stack) - 1
	destination_stack = int(destination_stack) - 1

	for k in range(nbMove):
		stacks[destination_stack].append(stacks[origine_stack].pop(-1 + k - nbMove + 1))

	indData += 1


result = ""

for i in range(len(stacks)):
	result += stacks[i][-1]

print(result)