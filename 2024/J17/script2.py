def combo_operand(operand):
	if operand <= 3:
		return operand

	return {
		4: reg_a,
		5: reg_b,
		6: reg_c
	}[operand]

def is_same(program, outputs):
	if len(program) != len(outputs):
		return False

	for i in range(len(program)):
		if program[i] != outputs[i]:
			return False

	return True

with open('input') as file:
	init_a = int(file.readline().split(': ')[1])
	init_b = int(file.readline().split(': ')[1])
	init_c = int(file.readline().split(': ')[1])
	file.readline()
	program = list(map(int, file.readline().split(': ')[1].split(',')))

not_found = True
init_a = 1

while not_found:
	reg_a = init_a
	reg_b = init_b
	reg_c = init_c

	outputs = []
	pointer = 0
	while pointer < len(program):
		instruction = program[pointer]
		operand = program[pointer + 1]
		have_jump = False

		match program[pointer]:
			case 0:
				reg_a = int(reg_a / 2**(combo_operand(operand)))
			case 1:
				reg_b = reg_b ^ operand
			case 2:
				reg_b = combo_operand(operand) % 8
			case 3:
				if reg_a != 0:
					pointer = operand
					have_jump = True
			case 4:
				reg_b = reg_b ^ reg_c
			case 5:
				outputs.append(combo_operand(operand) % 8)
			case 6:
				reg_b = int(reg_a / 2**(combo_operand(operand)))
			case 7:
				reg_c = int(reg_a / 2**(combo_operand(operand)))

		if not(have_jump):
			pointer += 2

	if is_same(program, outputs):
		not_found = False
	else:
		init_a += 1

print(init_a)
