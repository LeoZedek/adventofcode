from collections import defaultdict

with open("input") as file:
  data = file.readlines()

after_it = defaultdict(list)

i = 0

while (data[i] != "\n"):
  before, after = list(map(int, data[i].split('|')))
  after_it[before].append(after)
  i += 1

r = 0
i += 1

while (i < len(data)):
  pages = list(map(int, data[i].split(',')))

  good_order = True

  for j in reversed(range(len(pages))):
    page_after = pages[j]
    for k in reversed(range(j)):
      page_before = pages[k]

      if page_before in after_it[page_after]:
        good_order = False

  if good_order:
    r += pages[len(pages) // 2]

  i += 1

print(r)