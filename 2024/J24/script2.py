from pyvis.network import Network

AND = 0
OR = 1
XOR = 2

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

net = Network(notebook = True, cdn_resources = "remote",
                bgcolor = "#222222",
                font_color = "white",
                height = "750px",
                width = "100%",
                directed= True
)

gates = {}

with open('input') as file:
	line = file.readline().strip()
	while line != '':
		gate, value =  line.split(': ')
		net.add_node(gate, shape = 'box', color='blue')
		line = file.readline().strip()

	line = file.readline().strip()
	while line != '':
		operation, gateId = line.split(' -> ')
		gateInput1Id, operator, gateInput2Id = operation.split(' ')

		net.add_node(gateId, shape='circle', color={
			'AND': 'red',
			'OR': 'green',
			'XOR': 'gray'
			}[operator])

		
		gates[gateId] = Gate(gateId, gateInput1Id, gateInput2Id, operator)

		line = file.readline().strip()

for gateId, gate in gates.items():
	net.add_edge(gate.gate1Id, gateId)
	net.add_edge(gate.gate2Id, gateId)

net.show("graph.html")

print(','.join(sorted(['z07', 'vmv', 'z20', 'kfm', 'tqr', 'hth', 'z28', 'hnv'])))