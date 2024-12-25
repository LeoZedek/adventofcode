from collections import defaultdict

def mix(secret, number):
	return secret ^ number

def prune(secret):
	return secret % 16777216

with open('input') as file:
	data = list(map(int, file.read().splitlines()))

bananas_selled = defaultdict(int)

for secret in data:
	changes = []
	previous = secret
	already_got = set()
	for i in range(2000):
		number = secret * 64
		secret = mix(secret, number)
		secret = prune(secret)

		number = secret // 32
		secret = mix(secret, number)
		secret = prune(secret)

		number = secret * 2048
		secret = mix(secret, number)
		secret = prune(secret)

		changes.append(secret % 10 - previous % 10)
		if len(changes) == 5:
			changes.pop(0)

		if len(changes) == 4:
			sequence = tuple(changes)
			if not(sequence in already_got):
				bananas_selled[sequence] += secret % 10
				already_got.add(sequence)

		previous = secret 

print(max(bananas_selled.values()))

