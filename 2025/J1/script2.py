with open('input', 'r') as file:
  data = file.readlines();

dial = 50;
result = 0;

for line in data:
	number = int(line[1:])
	result += number // 100
	number = number - (number // 100 * 100)
	if (line[0] == 'R'):
		dial += number
		if dial >= 100:
			result += 1
	else:
		if dial > 0 and dial - number <= 0:
			result += 1
		dial -= number;

	dial %= 100

print(result)