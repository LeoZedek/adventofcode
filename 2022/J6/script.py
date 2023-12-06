f = open('input')

data = f.readlines()

f.close()

signal = data[0].split('\n')[0]

lenght_marker = 14

i = lenght_marker - 1
done = False
result = 0

while not(done):
	if len(set(signal[i - lenght_marker + 1 : i + 1])) == lenght_marker:
		done = True
		result = i + 1

	i += 1

print(result)