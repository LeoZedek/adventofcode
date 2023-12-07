HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIR = 2
THREE_OF_A_KIND = 3
FULL_HOUSE = 4
FOUR_OF_A_KIND = 5
FIVE_OF_A_KIND = 6

CARD_ORDER = "23456789TJQKA"

class Hand:
	def __init__(self, cards, bid):
		self.cards = cards
		self.bid = int(bid)

	def __repr__(self):
		return "cards : " + self.cards + "\nbid : " + str(self.bid) + "\n"

with open("input", "r") as file:
	data = file.readlines()

hands = []

for line in data:
	hands.append(Hand(*line.split()))

def is_better_hand(hand1, hand2):

	# Well contain type of hand1 and hand2
	types = []

	cards1 = hand1.cards
	cards2 = hand2.cards

	for hand in [cards1, cards2]:

		set_hand = set([*hand])
		len_set = len(set_hand)
		
		if len_set == 1:
			hand_type = FIVE_OF_A_KIND

		elif len_set == 2:
			if hand.count(hand[0]) == 1 or hand.count(hand[0]) == 4:
				hand_type = FOUR_OF_A_KIND
			else:
				hand_type = FULL_HOUSE

		elif len_set == 3:
			find_three = False

			for letter in hand:
				if hand.count(letter) == 3:
					find_three = True

			if find_three:
				hand_type = THREE_OF_A_KIND
			else:
				hand_type = TWO_PAIR

		elif len_set == 4:
			hand_type = ONE_PAIR

		else:
			hand_type = HIGH_CARD

		types.append(hand_type)

	hand1_type = types[0]
	hand2_type = types[1]

	if hand1_type > hand2_type:
		return 1
	elif hand1_type < hand2_type:
		return -1

	else:

		for i in range(len(cards1)):
			if CARD_ORDER.index(cards1[i]) < CARD_ORDER.index(cards2[i]):
				return -1
			elif CARD_ORDER.index(cards1[i]) > CARD_ORDER.index(cards2[i]):
				return 1

		print("Should not happen")
		return 0

import functools

hand_sorted = sorted(hands, key=functools.cmp_to_key(is_better_hand))

result = 0

for i in range(len(hand_sorted)):
	result += hand_sorted[i].bid * (i + 1)

print(result)