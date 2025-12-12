with open('input', 'r') as file:
  data = file.readlines();

dial = 50;
result = 0;

for line in data:
	number = int(line[1:]);
	if (line[0] == 'R'):
		dial = (dial + number) % 100;
	else:
		dial = (dial - number) % 100;

	if dial == 0:
		result += 1;

print(result)