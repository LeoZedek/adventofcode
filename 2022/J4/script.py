f = open('input')

data = f.readlines()

f.close()

data = list(map(lambda x : x.split('\n')[0].split(','), data))

res1 = 0
res2 = 0

for i in range(len(data)):
	range_elf1 = data[i][0].split('-')
	range_elf1 = list(map(int, range_elf1))

	range_elf2 = data[i][1].split('-')
	range_elf2 = list(map(int, range_elf2))

	if (range_elf2[0] <= range_elf1[0] and range_elf1[1] <= range_elf2[1])\
		or (range_elf1[0] <= range_elf2[0] and range_elf2[1] <= range_elf1[1]):
		res1 += 1

	if not((range_elf1[0] < min(range_elf2) and range_elf1[1] < min(range_elf2))\
	or (range_elf2[0] < min(range_elf1) and range_elf2[1] < min(range_elf1))):
		res2 += 1

print(res1)
print(res2)