from collections import defaultdict

def search_order(pages, after_it):

  solution = []
  sol_page = None

  for page in pages:
    remainding_pages = pages.copy()
    remainding_pages.remove(page)
    temp_result = search_order_rec(page, remainding_pages, after_it)
    if len(temp_result) > len(solution):
      solution = temp_result
      sol_page = page

  return [sol_page] + solution

def search_order_rec(page, remainding_pages, after_it):

  if len(remainding_pages) == 0:
    return []

  best_solution = []

  for remainding_page in remainding_pages:
    if remainding_page in after_it[page]:
      remainding_pages_copy = remainding_pages.copy()
      remainding_pages_copy.remove(remainding_page)

      temp = search_order_rec(remainding_page, remainding_pages_copy, after_it)

      if len(temp) == len(remainding_pages_copy):
        return [remainding_page] + temp

  return []

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

  if not(good_order):
    pages_order_good = search_order(pages, after_it)

    r += pages_order_good[len(pages_order_good)//2]
  i += 1

print(r)