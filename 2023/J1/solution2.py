digit = {
	"one": '1',
	"two": '2',
	"three": '3',
	"four": '4',
	"five": '5',
	"six": '6',
	"seven": '7',
	"eight": '8',
	"nine": '9'
}

def is_digit_num(s, i):
	for digit_num in digit:
		if s[i:i+len(digit_num)] == digit_num:
			return digit[digit_num]

	return ""

def find_digit(s, first = True):

	if first:
		i = 0
	else:
		i = len(s) - 1

	while not(s[i].isdigit() or is_digit_num(s, i)):
		if first:
			i += 1
		else:
			i -= 1

	if s[i].isdigit():
		return s[i]
	else:
		return is_digit_num(s, i)


with open("input", "r") as file:
	data = file.readlines()

result = 0

for chunk in data:

	number = find_digit(chunk, first=True)

	number += find_digit(chunk, first = False)

	result += int(number)

print(result)