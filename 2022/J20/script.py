import numpy as np

with open('input') as f:
	data = list(map(lambda x : int(x.split('\n')[0]), f.readlines()))

values = {}
encrypted_file = []
lenght = len(data)

decryption_key = 811589153

for index, number in enumerate(data):
	encrypted_file.append(index)
	values[index] = number

	if number == 0:
		identity_number_of_zero = index

for key in values:
	values[key] *= decryption_key

for i in range(10):

	for identity_number in range(lenght):

		old_index = encrypted_file.index(identity_number)

		new_index = (old_index + values[identity_number])

		new_index %= lenght - 1

		if new_index == 0 and values[identity_number] != 0:
			new_index = lenght - 1

		encrypted_file.pop(old_index)
		encrypted_file.insert(new_index, identity_number)

index_zero = encrypted_file.index(identity_number_of_zero)

index1 = (index_zero + 1000) % lenght
index2 = (index_zero + 2000) % lenght
index3 = (index_zero + 3000) % lenght

print(values[encrypted_file[index1]] + values[encrypted_file[index2]] + values[encrypted_file[index3]])
