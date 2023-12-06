with open("input", "r") as file:

	data = file.readlines()


time = int("".join(data[0].split(":")[1].strip().split()))

distance = int("".join(data[1].split(":")[1].strip().split()))

result = 0

for hold_time in range(time + 1):
	if hold_time * (time - hold_time) > distance:
		result += 1

print(result)