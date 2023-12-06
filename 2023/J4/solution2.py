with open("input", "r") as file:

	data = file.readlines()

number_cards = {}

for line in data:

	card_name, numbers = line.split(":")

	card_number = int(card_name.split()[1].strip())

	if not(card_number in number_cards):
		number_cards[card_number] = 1

	winning_numbers, my_numbers = numbers.split("|")
	winning_numbers = winning_numbers.strip()
	my_numbers = my_numbers.strip()

	winning_numbers = list(map(int, winning_numbers.split()))
	my_numbers = list(map(int, my_numbers.split()))

	number_match = 0

	for my_number in my_numbers:
		if my_number in winning_numbers:

			number_match += 1

	for card_won in range(1 + card_number, card_number + 1 + number_match):
		if not(card_won in number_cards):
			number_cards[card_won] = 1 + number_cards[card_number]
		else:
			number_cards[card_won] += number_cards[card_number]

print(sum(number_cards.values()))