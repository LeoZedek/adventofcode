def find_overlap(range1, range2):
	if range1.start > range2.end or range2.start > range1.end:
		return None

	return Pair_Range(max(range1.start, range2.start), min(range1.end, range2.end))

def remove_overlap(_range, range2):

	overlap = find_overlap(_range, range2)

	if overlap.start == _range.start and overlap.end == _range.end:
		return []

	if overlap.end == _range.end:
		return [Pair_Range(_range.start, overlap.start - 1)]

	if overlap.start == _range.start:
		return [Pair_Range(overlap.end + 1, _range.end)]

	return [Pair_Range(_range.start, overlap.start - 1), Pair_Range(overlap.end + 1, _range.end)]

def is_overlap(range1, range2):
	return not(range1.start > range2.end or range1.end < range2.start)

def separate(ranges, range2):

	intersection = []
	outside = []

	for _range in ranges:
		if is_overlap(_range, range2):
			without_overlap = remove_overlap(_range, range2)
			outside += without_overlap

			overlap = find_overlap(_range, range2)
			intersection.append(overlap)
		else:
			outside.append(_range)

	return intersection, outside

def remove_outside_overlaps(ranges, overlap):
	result = []

	for _range in ranges:
		if is_overlap(_range, overlap):
			overlap = find_overlap(_range, overlap)
			result.append(overlap)

	return result 

class Pair_Range:
	def __init__(self, start, value):
		self.start = start
		self.end = value

	@property
	def length(self):
		return self.end - self.start + 1
	

	def __repr__(self):
		return "[" + str(self.start) + ", " + str(self.end) + "]"

class Values_Range:

	def __init__(self, start_value, end_value, values = None):
		if values is None:
			self.values = [Pair_Range(start_value, end_value)]
		else:
			self.values = values

	def separate(self, range):
		inter, out = separate(self.values, range)

		return Values_Range(1, 1, inter), Values_Range(1, 1, out)

	def count(self):
		result = 0

		for pair_range in self.values:
			result += pair_range.length

		return result

	def __repr__(self):

		return str(self.values)

class Parts:

	def __init__(self, parts_value=None):
		if parts_value == None:
			self.parts_value = {
			"x": Values_Range(1, 4000),
			"m": Values_Range(1, 4000),
			"a": Values_Range(1, 4000),
			"s": Values_Range(1, 4000),
			}
		else:
			self.parts_value = parts_value

	def separate(self, part_name, range_meet_requirement):

		meet_requirement, dont_meet_requirement = self.parts_value[part_name].separate(range_meet_requirement)

		meet_parts = {}
		dont_meet_parts = {}

		for key, value in self.parts_value.items():
			if key == part_name:
				meet_parts[key] = meet_requirement
				dont_meet_parts[key] = dont_meet_requirement

			else:
				meet_parts[key] = value
				dont_meet_parts[key] = value

		return Parts(meet_parts), Parts(dont_meet_parts)

	def count(self):
		result = 1

		for value in self.parts_value.values():
			result *= value.count()
		return result

	def __repr__(self):
		return str(self.parts_value)

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

	def __repr__(self):
		return self.part + self.compare + str(self.value) + ":" + self.next_workflow

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

	def number_accepted(self, parts, workflows):

		result = 0

		for rule in self.rules:

			if isinstance(rule, ComparaisonRule):
				if rule.compare == "<":
					range_meet_requirement = Pair_Range(1, rule.value - 1)
				else:
					range_meet_requirement = Pair_Range(rule.value + 1, 4000)

				meet_parts, dont_meet_parts = parts.separate(rule.part, range_meet_requirement)

				if rule.next_workflow == "R":
					result += 0
				elif rule.next_workflow == "A":
					result += meet_parts.count()
				else:
					result += workflows[rule.next_workflow].number_accepted(meet_parts, workflows)

				parts = dont_meet_parts

			else:

				if rule == "R":
					result += 0
				elif rule == "A":
					result += parts.count()
				else:
					result += workflows[rule].number_accepted(parts, workflows)


		return result


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

print(workflows["in"].number_accepted(Parts(), workflows))