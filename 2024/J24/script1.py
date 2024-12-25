AND = 0
OR = 1
XOR = 2

class InitGate:
	def __init__(self, value):
		self.value = value

	def get_value(self):
		return self.value

class Gate:
	def __init__(self, _id, gate1Id, gate2Id, operator):
		self.id = _id
		self.gate1Id = gate1Id
		self.gate2Id = gate2Id
		self.operator = operator
		self.value = None

	def get_value(self):
		if self.value == None:
			self.value = self.compute(gates[self.gate1Id].get_value(), gates[self.gate2Id].get_value())
		return self.value

	def compute(self, value1, value2):

		if self.operator == AND:
			return value1 & value2
		elif self.operator == OR:
			return value1 | value2
		else:
			return value1 ^ value2

gates = {}
gates_z = []

with open('input') as file:
	line = file.readline().strip()
	while line != '':
		gate, value =  line.split(': ')
		gates[gate] = InitGate(bool(int(value)))
		line = file.readline().strip()

	line = file.readline().strip()
	while line != '':
		operation, gateId = line.split(' -> ')
		gateInput1Id, operator, gateInput2Id = operation.split(' ')

		operator = {
			'AND': AND,
			'OR': OR,
			'XOR': XOR
		}[operator]

		if gateId[0] == 'z':
			gates_z.append(Gate(gateId, gateInput1Id, gateInput2Id, operator))
		else:
			gates[gateId] = Gate(gateId, gateInput1Id, gateInput2Id, operator)

		line = file.readline().strip()

gates_z.sort(reverse = True, key = lambda x : x.id)

binary_result = []
for gate in gates_z:
	binary_result.append({False: '0', True: '1'}[gate.get_value()])

print(int(''.join(binary_result), 2))