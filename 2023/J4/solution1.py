with open("input", "r") as file:

	data = file.readlines()

result = 0

for line in data:

	card_name, numbers = line.split(":")

	card_number = int(card_name.split()[1].strip())

	winning_numbers, my_numbers = numbers.split("|")
	winning_numbers = winning_numbers.strip()
	my_numbers = my_numbers.strip()

	winning_numbers = list(map(int, winning_numbers.split()))
	my_numbers = list(map(int, my_numbers.split()))

	card_score = 0

	for my_number in my_numbers:
		if my_number in winning_numbers:
			if card_score == 0:
				card_score = 1
			else:
				card_score *= 2

	result += card_score

print(result)