f = open('input')

data = list(map(lambda x: x.split('\n')[0], f.readlines()))

f.close()

def distance_inf(pos1, pos2):
	return max(abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1]))

def distance_euclidienne(pos1, pos2):
	return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def new_pos(head, tail):

	if head[0] == tail[0] or head[1] == tail[1]:
		tail_possible_pos = [
			(head[0] - 1, head[1]),
			(head[0] + 1, head[1]),
			(head[0], head[1] + 1),
			(head[0], head[1] - 1),

		]

		return min(tail_possible_pos, key = lambda x : distance_euclidienne(x, tail))

	else:
		tail_possible_pos = [
			(tail[0] - 1, tail[1] - 1),
			(tail[0] + 1, tail[1] - 1),
			(tail[0] + 1, tail[1] + 1),
			(tail[0] - 1, tail[1] + 1),
		]

		return min(tail_possible_pos, key = lambda x : distance_euclidienne(x, head))


tails_pos = []
head_pos = (0, 0)

tail_pos_set = set()
tail_pos_set.add((0, 0))

for k in range(9):
	tails_pos.append((0, 0))
print(len(tails_pos))

for ind, string in enumerate(data):

	direction = string.split(' ')[0]
	nbStep = int(string.split(' ')[1])

	for k in range(nbStep):

		if direction == "R":
			head_pos = (head_pos[0], head_pos[1] + 1)

		if direction == "L":

			head_pos = (head_pos[0], head_pos[1] - 1)

		if direction == "D":

			head_pos = (head_pos[0] + 1, head_pos[1])

		if direction == "U":

			head_pos = (head_pos[0] - 1, head_pos[1])

		for i in range(len(tails_pos)):
			if i != 0:
				temp_head = tails_pos[i - 1]

			else:
				temp_head = head_pos

			temp_tail = tails_pos[i]

			if distance_inf(temp_head, temp_tail) > 1:
				new_tail_pos = new_pos(temp_head, temp_tail)
				tails_pos[i] = new_tail_pos

				if i == len(tails_pos) - 1:
					tail_pos_set.add(new_tail_pos)

print("result 2 :", str(len(tail_pos_set)))