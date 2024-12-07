UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

DELTA = {
  UP: (-1, 0),
  RIGHT: (0, 1),
  DOWN: (1, 0),
  LEFT: (0, -1)
}

def turn_right(direction):
  return DIRECTIONS[(DIRECTIONS.index(direction) + 1) % len(DIRECTIONS)]

def move(row, col, direction):
  return row + DELTA[direction][0], col + DELTA[direction][1]

def in_loop(start, direction, new_block):
  row, col = start

  visited_square = {(row, col, direction)}

  while data[row][col] != '*':
      
    temp_r, temp_col = move(row, col, direction)

    if data[temp_r][temp_col] != '#' and (temp_r, temp_col) != new_block:
      row, col = temp_r, temp_col
      if (row, col, direction) in visited_square:
        return True
      visited_square.add((row, col, direction))
    else:
      direction = turn_right(direction)
      visited_square.add((row, col, direction))

  return False

with open("input") as file:
  data = file.readlines()

for i in range(len(data)):
  data[i] = '*' + data[i].strip() + '*'

data.append('*' * len(data[0]))
data.insert(0, '*' * len(data[0]))

for i in range(len(data)):
  for j in range(len(data[i])):
    if data[i][j] == '^':
      start_row, start_col = (i, j)

direction = UP
visited_square = {(start_row, start_col)}

r = 0

row, col = start_row, start_col
while data[row][col] != '*':

  temp_r, temp_col = move(row, col, direction)
  if data[temp_r][temp_col] != '#':
    if (temp_r, temp_col) != (start_row, start_col)\
    and data[temp_r][temp_col] != '*'\
    and not((temp_r, temp_col) in visited_square)\
    and in_loop((row, col), direction, (temp_r, temp_col)):
      r += 1
    row, col = temp_r, temp_col
    visited_square.add((row, col))
  else:
    direction = turn_right(direction)

print(r)
