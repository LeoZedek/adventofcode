def hash(step):
	result = 0

	for char in step:
		result += ord(char)
		result *= 17
		result %= 256

	return result

with open("input", "r") as file:
	line = file.readline().strip()

steps = line.split(",")

lens_focal_length = {}
boxes = {}

for step in steps:


	if step[-1] == "-":
		lens_label = step[:-1]
		boxe_number = hash(lens_label)

		if boxe_number in boxes and lens_label in boxes[boxe_number]:
			boxes[boxe_number].remove(lens_label)

	else:
		lens_label, focal_length = step.split("=")
		focal_length = int(focal_length)
		boxe_number = hash(lens_label)

		if not(boxe_number) in boxes:
			boxes[boxe_number] = []

		if not(lens_label in boxes[boxe_number]):
			boxes[boxe_number].append(lens_label)
		
		lens_focal_length[lens_label] = focal_length

result = 0

for boxe_number, lens in boxes.items():

	for i in range(len(lens)):
		result += (boxe_number + 1) * (i + 1) * (lens_focal_length[lens[i]])

print(result)