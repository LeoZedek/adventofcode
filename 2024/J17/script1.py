def combo_operand(operand):
	if operand <= 3:
		return operand

	return {
		4: reg_a,
		5: reg_b,
		6: reg_c
	}[operand]

with open('input') as file:
	reg_a = int(file.readline().split(': ')[1])
	reg_b = int(file.readline().split(': ')[1])
	reg_c = int(file.readline().split(': ')[1])
	file.readline()
	program = list(map(int, file.readline().split(': ')[1].split(',')))

outputs = []
pointer = 0
while pointer < len(program):
	instruction = program[pointer]
	operand = program[pointer + 1]
	have_jump = False

	print(program[pointer])

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
			outputs.append(str(combo_operand(operand) % 8))
			print(reg_a, reg_b, reg_c)
		case 6:
			reg_b = int(reg_a / 2**(combo_operand(operand)))
		case 7:
			reg_c = int(reg_a / 2**(combo_operand(operand)))

	if not(have_jump):
		pointer += 2
print(program)
print(','.join(outputs))