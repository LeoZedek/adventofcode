f = open('input')

data = f.readlines()

f.close()

for i in range(len(data)):
	data[i] = data[i].split('\n')[0]

def common_char(string1, string2, string3):

	for char in string1:
		if char in string2 and char in string3:
			return char

	return False

result = 0

for i in range(len(data)//3):

	common_item = common_char(data[i * 3], data[i * 3 + 1], data[i * 3 + 2])

	if 'a' <= common_item and common_item <= 'z':
		result += ord(common_item) - 96

	else:
		result += ord(common_item) - 38

print(result)