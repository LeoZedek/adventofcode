LOW = 0
HIGH = 1

ON = 0
OFF = 1

class Pulse:
	def __init__(self, power, input_module, destination_module):
		self.power = power
		self.input_module = input_module
		self.destination_module = destination_module

	def __repr__(self):
		return str(self.input_module) + " -" + str({LOW: "low", HIGH: "high"}[self.power]) + " -> " + str(self.destination_module)


class Flip_flop:

	def __init__(self, name):
		self.name = name
		self.destination_modules = []
		self.state = OFF

	def add_destination_module(self, module):
		self.destination_modules.append(module)

	def pulse(self, pulse):

		if pulse.power == HIGH:
			return []

		else:

			result = []

			pulse_power = {OFF: HIGH, ON: LOW}[self.state]

			for destination_module in self.destination_modules:
				result.append(Pulse(pulse_power, self, destination_module))

			self.state = {ON: OFF, OFF: ON}[self.state]

			return result

	def __repr__(self):
		return self.name

class Conjonction:

	def __init__(self, name):
		self.name = name
		self.input_modules_memory = {}
		self.destination_modules = []

	def add_destination_module(self, destination_module):
		self.destination_modules.append(destination_module)

	def add_input_module(self, input_module):
		self.input_modules_memory[input_module] = LOW

	def all_memory_high(self):

		for state in self.input_modules_memory.values():
			if state == LOW:
				return False

		return True

	def pulse(self, pulse):

		self.input_modules_memory[pulse.input_module] = pulse.power

		if self.all_memory_high():
			power = LOW
		else:
			power = HIGH

		result = []

		for destination_module in self.destination_modules:
				result.append(Pulse(power, self, destination_module))

		return result

	def __repr__(self):
		return self.name

class Broadcast:

	def __init__(self, name):
		self.name = name
		self.destination_modules = []

	def add_destination_module(self, destination_module):
		self.destination_modules.append(destination_module)

	def pulse(self, pulse):
		result = []

		for destination_module in self.destination_modules:
				result.append(Pulse(pulse.power, self, destination_module))

		return result

	def __repr__(self):
		return self.name

class Machine:

	def __init__(self):
		self.name = "rx"

	def pulse(self, pulse):
		return []

	def __repr__(self):
		return self.name

class Button:

	def __init__(self):
		self.name = "button"

	def __repr__(self):
		return self.name

def one_is_None(dictionary):
	for value in dictionary.values():
		if value == None:
			return True

	return False

with open("input", "r") as file:

	data = file.readlines()

for i in range(len(data)):
	data[i] = data[i].strip()

modules = {}

for line in data:

	name = line.split(" -> ")[0]

	if name[0] == "%":

		modules[name[1:]] = Flip_flop(name[1:])

	elif name[0] == "&":

		modules[name[1:]] = Conjonction(name[1:])

	else:

		modules[name] = Broadcast(name)

machine = Machine()

for line in data:

	name_module, string_name_destination_modules = line.split(" -> ")

	name_destination_modules = string_name_destination_modules.split(", ")

	if name_module != "broadcaster":
		name_module = name_module[1:]

	module = modules[name_module]

	for name_destination_module in name_destination_modules:
		if name_destination_module in modules:
			destination_module = modules[name_destination_module]
		else:
			destination_module = machine

		module.add_destination_module(destination_module)

		if isinstance(destination_module, Conjonction):
			destination_module.add_input_module(module)

broadcast_module = modules["broadcaster"]

# See visualization to understand this
first_high_pulse = {
	"bg": None,
	"ls": None,
	"sj": None,
	"qq": None
}

i = 0
while one_is_None(first_high_pulse):

	i += 1

	pulses_queue = [Pulse(LOW, Button(), broadcast_module)]

	while len(pulses_queue) > 0:

		current_pulse = pulses_queue.pop(0)

		pulses_queue += current_pulse.destination_module.pulse(current_pulse)

		if current_pulse.input_module.name in first_high_pulse and current_pulse.power == HIGH:
			first_high_pulse[current_pulse.input_module.name] = i


list_value = list(first_high_pulse.values())

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

def lcm(a, b):
	return (a / gcd(a, b)) * b

result = list_value.pop(0)

for value in list_value:
	result = lcm(result, value)

print(int(result))