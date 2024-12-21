class Result:
	def __init__(self, init_value):
		self.result = init_value

	def add(self):
		self.result += 1

class Stone_Tree:
	def __init__(self, left, right):
		self.left = left
		self.right = right

	def blink(self, result):
		if isinstance(self.left, int):
			string_val = str(self.left)
			if self.left == 0:
				self.left = 1
			elif len(string_val) % 2 == 0:
				self.left = Stone_Tree(int(string_val[:len(string_val)//2]), int(string_val[len(string_val)//2:])) 
				result.add()
			else:
				self.left *= 2024
		else:
			self.left.blink(result)

		if isinstance(self.right, int):
			string_val = str(self.right)
			if self.right == 0:
				self.right = 1
			elif len(string_val) % 2 == 0:
				self.right = Stone_Tree(int(string_val[:len(string_val)//2]), int(string_val[len(string_val)//2:])) 
				result.add()
			else:
				self.right *= 2024
		else:
			self.right.blink(result)

with open('input') as file:
	data = file.read().strip()

stones = list(map(int, data.split()))

r = Result(len(stones))

stones_trees = []

i = 0
while i < len(stones) - 1:
	stones_trees.append(Stone_Tree(stones[i], stones[i+1]))
	i += 2

for i in range(25):
	for stone in stones_trees:
		stone.blink(r)

print(r.result)