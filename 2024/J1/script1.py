with open('input', 'r') as file:
  data = file.readlines()

t1 = []
t2 = []

for line in data:
  item1, item2 = line.split("   ")

  t1.append(int(item1))
  t2.append(int(item2))

t1.sort()
t2.sort()

r = 0

for i in range(len(t1)):
  r += abs(t1[i] - t2[i])

print(r)