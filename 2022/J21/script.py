with open('input') as f:
	data = list(map(lambda x: x.split('\n')[0], f.readlines()))

RIGHT = 0
LEFT = 1

class Monkey_number():

	def __init__(self, name, number):
		self.name = name

		self.number = number

	def yell(self):
		return self.number

	def have_human(self):
		if self.name == "humn":
			return True

		return False

	def is_human(self):
		return self.name == "humn"

	def __repr__(self):
		return "{} -> {}".format(self.name, self.number)

class Monkey_operation():

	def __init__(self, name, name_monkey_left, operation, name_monkey_right):
		self.name = name
		self.name_monkey_left = name_monkey_left
		self.name_monkey_right = name_monkey_right
		self.operation = operation
		self.monkey_left = None
		self.monkey_right = None

	def yell(self):

		if self.operation == "+":
			result = self.monkey_left.yell() + self.monkey_right.yell()

		elif self.operation == "-":
			result = self.monkey_left.yell() - self.monkey_right.yell()

		elif self.operation == "*":
			result = self.monkey_left.yell() * self.monkey_right.yell()

		elif self.operation == "/":
			result = self.monkey_left.yell() / self.monkey_right.yell()
		else:
			print("error operation")

		return result

	def set_left(self, monkey):
		self.monkey_left = monkey

	def set_right(self, monkey):
		self.monkey_right = monkey

	def have_human(self):
		if self.name == "humn":
			return True

		return self.monkey_left.have_human() or self.monkey_right.have_human()

	def is_human(self):
		return self.name == "humn"

	def __repr__(self):
		return "{} -> {} {} {}".format(self.name, self.name_monkey_left, self.operation, self.name_monkey_right)


monkeys = {}

for ind, string_data in enumerate(data):

	string_list = string_data.split(' ')

	if len(string_list) > 2:
		name = string_list[0][:-1]
		left = string_list[1]
		operation = string_list[2]
		right = string_list[3]

		monkey = Monkey_operation(name, left, operation, right)
		monkeys[name] = monkey

	else:
		name = string_list[0][:-1]
		number = int(string_list[1])
		monkey = Monkey_number(name, number)
		monkeys[name] = monkey

for monkey in monkeys.values():

	if isinstance(monkey, Monkey_operation):
		monkey.set_left(monkeys[monkey.name_monkey_left])
		monkey.set_right(monkeys[monkey.name_monkey_right])

root_monkey = monkeys["root"]

print("result 1 :",root_monkey.yell())

if root_monkey.monkey_left.have_human():
	number_to_have = root_monkey.monkey_right.yell()
	next_monkey = root_monkey.monkey_left
	position_next_monkey = LEFT

else:
	number_to_have = root_monkey.monkey_left.yell()
	next_monkey = root_monkey.monkey_right
	position_next_monkey = LEFT

while not(next_monkey.is_human()):
	right_monkey = next_monkey.monkey_right
	left_monkey = next_monkey.monkey_left
	operation = next_monkey.operation

	if next_monkey.monkey_left.have_human():

		right_monkey_yell = right_monkey.yell()

		if operation == "+":
			number_to_have -= right_monkey_yell

		elif operation == "-":
			number_to_have += right_monkey_yell

		elif operation == "*":
			number_to_have /= right_monkey_yell

		else:
			number_to_have *= right_monkey_yell

		next_monkey = next_monkey.monkey_left

	else:

		left_monkey_yell = left_monkey.yell()

		if operation == "+":
			number_to_have -= left_monkey_yell

		elif operation == "-":
			number_to_have = left_monkey_yell - number_to_have

		elif operation == "*":
			number_to_have /= left_monkey_yell

		else:
			number_to_have = left_monkey_yell / number_to_have

		next_monkey = next_monkey.monkey_right

print("result 2:", number_to_have)