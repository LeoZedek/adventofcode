from pyvis.network import Network

net = Network(directed = True)

with open("input", "r") as file:

	data = file.readlines()

for i in range(len(data)):
	data[i] = data[i].strip()

modules = {}

for line in data:

	name = line.split(" -> ")[0]

	if name[0] == "%":
		net.add_node(name[1:], label=name[1:], color = "blue")

	elif name[0] == "&":
		net.add_node(name[1:], label=name[1:], color = "red")

	else:
		net.add_node(name, label=name, color = "gray")

net.add_node("rx", label="rx", color = "black")

for line in data:

	name_module, string_name_destination_modules = line.split(" -> ")

	name_destination_modules = string_name_destination_modules.split(", ")

	if name_module != "broadcaster":
		name_module = name_module[1:]

	for destination_module in name_destination_modules:
		net.add_edge(name_module, destination_module)

net.show('visualization.html', notebook=False)
