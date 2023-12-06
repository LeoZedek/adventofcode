from math import floor

f = open('input')

data = list(map(lambda x : x.split('\n')[0], f.readlines()))

f.close()

class Monkey():

	def __init__(self):

		self.items = []
		self.operation = None
		self.monkeyToThrowIfTrue = None
		self.monkeyToThrowIfFalse = None
		self.divisibleIntTest = None

	def get_items(self):
		return self.items

	def append_item(self, item):
		self.items.append(item)

	def pop_item(self):
		return self.items.pop(0)

	def set_operation(self, operation):
		self.operation = operation

	def set_monkey_true(self, monkey):
		self.monkeyToThrowIfTrue = monkey

	def set_monkey_false(self, monkey):
		self.monkeyToThrowIfFalse = monkey

	def get_monkey_true(self):
		return self.monkeyToThrowIfTrue

	def get_monkey_false(self):
		return self.monkeyToThrowIfFalse

	def set_divisible_test(self, integer):
		self.divisibleIntTest = integer

		#for i in range(len(self.items)):
		#	self.items[i] %= integer

	def update_firts_worry_level_item(self, multiplie_of_all_level):
		new_level = self.items[0]
		operation = self.operation

		if operation[2] == "old":

			deuxieme_operande = self.items[0]

		else:
			deuxieme_operande = int(operation[2])

		if operation[1] == "+":

			new_level += deuxieme_operande

		elif operation[1] == "-":

			new_level -= deuxieme_operande

		elif operation[1] == "*":
			new_level *= deuxieme_operande

		else:

			print("error")
		#new_level = floor(new_level / 3)
		self.items[0] = new_level % multiplie_of_all_level

monkeys = []

for k in range((len(data) + 1) // 7):
	monkeys.append(Monkey())

for i in range(len(data)):
	ligne = data[i]

	ligne_split = ligne.split(' ')

	if len(ligne_split) > 1:

		if ligne_split[0] == "Monkey":

			id_monkey = int(ligne_split[1].split(':')[0])
			monkey = monkeys[id_monkey]

		elif ligne_split[2] == "Starting":

			for ind_items in range(4, len(ligne_split)):
				monkey.append_item(int(ligne_split[ind_items].split(',')[0]))

		elif ligne_split[2] == "Operation:":

			monkey.set_operation(ligne_split[-3:])

		elif ligne_split[2] == "Test:":
			monkey.set_divisible_test(int(ligne_split[-1]))

		elif ligne_split[4] == "If":

			if ligne_split[5] == "true:":
				monkey.set_monkey_true(monkeys[int(ligne_split[-1])])

			else:
				monkey.set_monkey_false(monkeys[int(ligne_split[-1])])

monkeys_inspect_time = [0] * len(monkeys)
all_level = 1

for i in range(len(monkeys)):
	all_level *= monkeys[i].divisibleIntTest

for k in range(10000):

	for ind_monkey, monkey in enumerate(monkeys):

		while len(monkey.get_items()) > 0:

			monkey.update_firts_worry_level_item(all_level)

			if monkey.get_items()[0] % monkey.divisibleIntTest == 0:
				monkey_catching = monkey.get_monkey_true()
			else:
				monkey_catching = monkey.get_monkey_false()

			monkey_catching.append_item(monkey.pop_item())
			#monkey_catching.append_item(monkey.pop_item())

			monkeys_inspect_time[ind_monkey] += 1

#	print("\nround {}:".format(k))
#	for ind_monkey, monkey in enumerate(monkeys):
#		print("Monkey {}: {}".format(ind_monkey, monkey.get_items()))

monkeys_inspect_time.sort()

print(monkeys_inspect_time[-1] * monkeys_inspect_time[-2])