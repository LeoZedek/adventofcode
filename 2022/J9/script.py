f = open('input')

data = list(map(lambda x: x.split('\n')[0], f.readlines()))

f.close()

def distance_inf(pos1, pos2):
	return max(abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1]))

def distance_euclidienne(pos1, pos2):
	return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def new_pos(head, tail):

	if distance_euclidienne(head, tail) == 3:

		tail_possible_pos = [
			(tail[0] - 1, tail[1] - 1),
			(tail[0] + 1, tail[1] - 1),
			(tail[0] + 1, tail[1] + 1),
			(tail[0] - 1, tail[1] + 1),
		]

		return min(tail_possible_pos, key = lambda x : distance_euclidienne(x, head))

	else:

		tail_possible_pos = [
			(head[0] - 1, head[1]),
			(head[0] + 1, head[1]),
			(head[0], head[1] + 1),
			(head[0], head[1] - 1),
		]

		return min(tail_possible_pos, key = lambda x : distance_euclidienne(x, tail))

head_pos = (0, 0)
tail_pos = (0, 0)

tail_pos_set = set()
tail_pos_set.add(tail_pos)

for ind, string in enumerate(data):

	direction = string.split(' ')[0]
	nbStep = int(string.split(' ')[1])
	
	for k in range(nbStep):

		if direction == "R":

			head_pos = (head_pos[0], head_pos[1] + 1)
			if distance_inf(head_pos, tail_pos) > 1:
				tail_pos = new_pos(head_pos, tail_pos)

		if direction == "L":

			head_pos = (head_pos[0], head_pos[1] - 1)
			if distance_inf(head_pos, tail_pos) > 1:
				tail_pos = new_pos(head_pos, tail_pos)

		if direction == "D":

			head_pos = (head_pos[0] + 1, head_pos[1])
			if distance_inf(head_pos, tail_pos) > 1:
				tail_pos = new_pos(head_pos, tail_pos)

		if direction == "U":

			head_pos = (head_pos[0] - 1, head_pos[1])
			if distance_inf(head_pos, tail_pos) > 1:
				tail_pos = new_pos(head_pos, tail_pos)

		tail_pos_set.add(tail_pos)

print("result 1 :", str(len(tail_pos_set)))
