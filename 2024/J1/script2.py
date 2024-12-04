with open('input', 'r') as file:
  data = file.readlines()

t1 = []
t2 = []

for line in data:
  item1, item2 = line.split("   ")

  t1.append(int(item1))
  t2.append(int(item2))

r = 0

for item in t1:
  r += item * t2.count(item)

print(r)