f = open('input')

data = f.readlines()

f.close()

for i in range(len(data)):
	data[i] = data[i].split('\n')[0]

def common_char(string1, string2):

	for char in string1:
		if char in string2:
			return char

	return False

result = 0

for string in data:
	compartement1 = string[0 : len(string)//2]
	compartement2 = string[len(string)//2 :]

	common_item = common_char(compartement1, compartement2)

	if 'a' <= common_item and common_item <= 'z':
		result += ord(common_item) - 96

	else:
		result += ord(common_item) - 38

print(result)