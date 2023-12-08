class Element:
	def __init__(self, left, right):
		self.left = left
		self.right = right

def all_finish(nodes):
	for node in nodes:
		if node[-1] != 'Z':
			return False

	return True

def all_same(l):
	n = l[0]

	for elt in l:
		if elt != n:
			return False

	return True

with open("input", "r") as file:
	data = file.readlines()

instructions = data[0].strip()

nodes = {}

start_nodes = []

path_to_end_length = {}

for i in range(2, len(data)):
	node, left_right = data[i].split(" = ")

	left, right = left_right.strip().strip(")").strip("(").split(", ")

	nodes[node] = Element(left, right)

	if node[-1] == 'A':
		start_nodes.append(node)

step = 0

for start_node in start_nodes:

	current_node = start_node

	step = 0

	while current_node[-1] != 'Z':

		instruction = instructions[step % len(instructions)]

		if instruction == "L":
			current_node = nodes[current_node].left
		elif instruction == "R":
			current_node = nodes[current_node].right
		else:
			print("should not happen")
			assert(1 != 1)

		step += 1

	path_to_end_length[start_node] = step

list_value = list(path_to_end_length.values())

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

def lcm(a, b):
	return (a / gcd(a, b)) * b

result = list_value.pop(0)

for value in list_value:
	result = lcm(result, value)

print(result)
