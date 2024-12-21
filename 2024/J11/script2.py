import math

def compute_number_stone(stone, number_blink, memo):
	key = (stone, number_blink)

	if key in memo:
		return memo[key]

	if number_blink == 0:
		return 1

	if stone == 0:
		memo[key] = compute_number_stone(1, number_blink - 1, memo)
		return memo[key]
	else:
		digits = int(math.log10(stone))+1
		if digits % 2 == 0:
			memo[key] = compute_number_stone(stone // 10**(digits // 2), number_blink - 1, memo) + compute_number_stone(stone % 10**(digits // 2), number_blink - 1, memo)
			return memo[key]
		else:
			memo[key] = compute_number_stone(stone * 2024, number_blink - 1, memo)
			return memo[key]

with open('input') as file:
	data = file.read().strip()

stones = list(map(int, data.split()))

r = 0
memo = {}

for stone in stones:
	r += compute_number_stone(stone, 75, memo)

print(r)