from functools import cache

with open("input", "r") as file:
	data = file.readlines()

groups = []

conditions = []

for line in data:
	line = line.strip()

	condition, group = line.split()

	group = list(map(int, group.split(",")))

	groups.append(tuple(group * 5))
	conditions.append("?".join([condition] * 5))
	# groups.append(tuple(group))
	# conditions.append(condition)

result = 0
n = []

@cache
def number_arrangement(condition, group):

	if len(condition) == 0:
		if len(group) == 0:
			return 1
		else:
			return 0

	if condition[0] == ".":
		if len(condition) == 1:
			return number_arrangement("", group)
		else:
			return number_arrangement(condition[1:], group)

	elif condition[0] == "?":
		if len(condition) == 1:
			return number_arrangement("", group) + number_arrangement("#", group)
		else:
			return number_arrangement(condition[1:], group) + number_arrangement("#" + condition[1:], group)

	elif condition[0] == "#":
		if len(group) == 0:
			return 0

		number_broken = 1

		i = 1
		while i < len(condition) and condition[i] == "#":
			i += 1
			number_broken += 1

		if number_broken > group[0]:
			return 0

		elif number_broken < group[0]:
			if i == len(condition) or condition[i] == ".":
				return 0

			else: # condition[i] == "?"
				if i == len(condition) - 1:
					return number_arrangement(condition[:i] + "#", group)
				else:
					return number_arrangement(condition[:i] + "#" + condition[i+1:], group)

		elif number_broken == group[0]:

			if i == len(condition) - 1 or i == len(condition):
				if len(group) > 0:
					return number_arrangement("", group[1:])
				else:
					return number_arrangement("", [])

			else:
				if len(group) > 0:

					return number_arrangement(condition[i+1:], group[1:])
				else:
					return number_arrangement(condition[i+1:], [])

result = 0

for i in range(len(groups)):

	condition = conditions[i]
	group = groups[i]

	result += number_arrangement(condition, group)
print(result)