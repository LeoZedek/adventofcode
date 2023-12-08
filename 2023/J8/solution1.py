with open("input", "r") as file:
	data = file.readlines()

instructions = data[0].strip()

class Element:
	def __init__(self, left, right):
		self.left = left
		self.right = right

nodes = {}

for i in range(2, len(data)):
	node, left_right = data[i].split(" = ")

	left, right = left_right.strip().strip(")").strip("(").split(", ")

	nodes[node] = Element(left, right)

current_node = "AAA"

step = 0

while current_node != "ZZZ":

	instruction = instructions[step % len(instructions)]

	if instruction == "L":
		current_node = nodes[current_node].left
	elif instruction == "R":
		current_node = nodes[current_node].right
	else:
		print("should not happen")
		assert(1 != 1)

	step += 1

print(step)