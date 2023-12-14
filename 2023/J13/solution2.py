def find_mirror_row(pattern):

	result = []

	for i in range(1, len(pattern)):

		match = True

		up_row_index = i - 1
		down_row_index = i

		while down_row_index < len(pattern) and up_row_index >= 0 and match:

			if pattern[up_row_index] != pattern[down_row_index]:
				match = False

			up_row_index -= 1
			down_row_index += 1

		if match:
			result.append(i)

	return result

def get_column(tab, index):

	result = ""

	for i in range(len(tab)):

		result += tab[i][index]

	return result

def find_mirror_column(pattern):

	result = []

	for j in range(1, len(pattern[0])):

		match = True

		left_column_index = j - 1
		right_column_index = j

		while left_column_index >= 0 and right_column_index < len(pattern[0]):

			left_column = get_column(pattern, left_column_index)
			rigth_column = get_column(pattern, right_column_index)

			if left_column != rigth_column:
				match = False

			left_column_index -= 1
			right_column_index += 1

		if match:
			result.append(j)

	return result

def find_mirror_score(pattern):
	result = []

	mirror_rows = find_mirror_row(pattern)

	for row in mirror_rows:
		result.append(row * 100)

	result += find_mirror_column(pattern)

	return result

def replace_by_index(string, j):
	if string[j] == "#":
		return string[:j] + "." + string[j+1:]

	else:
		return string[:j] + "#" + string[j+1:]

with open("input", "r") as file:

	data = file.readlines()

for i in range(len(data)):
	data[i] = data[i].strip()

patterns = []

temp = []

for line in data:

	if line == "":
		patterns.append(temp)
		temp = []

	else:
		temp.append(line)

patterns.append(temp)

result = 0

for pattern in patterns:

	original_score = find_mirror_score(pattern)

	for i in range(len(pattern)):
		for j in range(len(pattern[i])):

			copy_pattern = pattern.copy()

			copy_pattern[i] = replace_by_index(copy_pattern[i], j)

			new_scores = find_mirror_score(copy_pattern)

			for score in new_scores:
				if not(score in original_score):
					result += score

print(result // 2)