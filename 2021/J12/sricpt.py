f = open('input')

data = f.readlines()

f.close()

for i in range(len(data)):
	data[i] = data[i].split('\n')[0].split('-')

