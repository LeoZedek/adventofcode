class Parts:

	def __init__(self, string_parts):

		self.parts_value = {}

		string_parts = string_parts[1:-2]

		for elt in string_parts.split(","):
			part, value = elt.split("=")

			self.parts_value[part] = int(value)

	def get(self, part):
		return self.parts_value[part]

	def sum_parts(self):
		return sum(self.parts_value.values())
	

class ComparaisonRule:

	def __init__(self, part, compare, value, next_workflow):

		self.part = part
		self.compare = compare
		self.value = value
		self.next_workflow = next_workflow

	def meet_requirement(self, parts):
		if self.compare == ">":
			return parts.get(self.part) > self.value
		else:
			return parts.get(self.part) < self.value

class Workflow:

	def __init__(self, workflow):

		rules = workflow.split(",")

		self.rules = []

		for rule in rules:
			if is_compare_rule(rule):

				compare, next_workflow = rule.split(":")

				self.rules.append(ComparaisonRule(compare[0], compare[1], int(compare[2:]), next_workflow))

			else:
				self.rules.append(rule)

	def is_accepted(self, parts, workflows):

		for rule in self.rules:

			if isinstance(rule, ComparaisonRule):

				if rule.meet_requirement(parts):

					if rule.next_workflow == "R":
						return False
					elif rule.next_workflow == "A":
						return True
					else:
						return workflows[rule.next_workflow].is_accepted(parts, workflows)

			else:

				if rule == "R":
					return False
				elif rule == "A":
					return True
				else:
					return workflows[rule].is_accepted(parts, workflows)


def is_compare_rule(rule):
	return ">" in rule or "<" in rule

with open("input", "r") as file:
	data = file.readlines()

i = 0

workflows = {}

while data[i] != "\n":

	line = data[i].strip("}\n")

	name, workflow = line.split("{")

	workflows[name] = Workflow(workflow)

	i += 1

i += 1

result = 0

while i < len(data):

	line = data[i]

	parts = Parts(line)

	if workflows["in"].is_accepted(parts, workflows):
		result += parts.sum_parts()

	i += 1

print(result)