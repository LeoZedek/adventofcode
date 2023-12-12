from itertools import permutations, combinations

def is_good_condition(condition, group):
	
	group = group.copy()

	group_length_to_be_good = group.pop(0)
	in_group = False
	group_length = 0

	for i in range(len(condition)):
		char = condition[i]

		if char == '#':
			in_group = True
			group_length += 1

		elif char == "." and in_group == True:
			if group_length != group_length_to_be_good:
				return False
			else:
				if len(group) == 0:
					group_length_to_be_good = 0
				else:
					group_length_to_be_good = group.pop(0)

				group_length = 0
				in_group = False

	if len(group) > 0 or group_length != group_length_to_be_good:
		return False

	return True

def replace_by_index(string, index, char):

	result = ""
	rank_unknow = 0

	for i in range(len(string)):
		if string[i] == "?":
			if rank_unknow in index:
				result += char
			else:
				result += "."

			rank_unknow += 1

		else:
			result += string[i]

	return result

with open("input", "r") as file:
	data = file.readlines()

groups = []

conditions = []

for line in data:
	line = line.strip()

	condition, group = line.split()

	group = list(map(int, group.split(",")))

	groups.append(group)
	conditions.append(condition)

result = 0

for i in range(len(groups)):

	condition = conditions[i]
	group = groups[i]

	total_failure = sum(group)

	number_failure_to_add = total_failure - condition.count("#")
	number_unknow_state = condition.count("?")


	if not(number_failure_to_add > condition.count("?")):
		
		for combination in combinations(range(number_unknow_state), number_failure_to_add):

			candidate_condition = replace_by_index(condition, list(combination), "#")

			if (is_good_condition(candidate_condition, group)):
				result += 1


print(result)