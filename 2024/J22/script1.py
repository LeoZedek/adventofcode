def mix(secret, number):
	return secret ^ number

def prune(secret):
	return secret % 16777216

with open('input') as file:
	data = list(map(int, file.read().splitlines()))

r = 0

for secret in data:
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
	r += secret

print(r)