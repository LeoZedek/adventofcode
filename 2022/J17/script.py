with open("input") as f:
	data = f.readline()[:-1]

ROCK_REST = 0

class HorizontalLine():

	def __init__(self, left_bottom):

		self.left = left_bottom[0]
		self.bottom = left_bottom[1]

		self.rocks_relative_position = {
			(0, 0),
			(1, 0),
			(2, 0),
			(3, 0)
		}

class Cross():

	def __init__(self, left_bottom):

		self.left = left_bottom[0]
		self.bottom = left_bottom[1]

		self.rocks_relative_position = {
			(1, 0),
			(0, 1),
			(1, 1),
			(2, 1),
			(1, 2)
		}


class LShape():

	def __init__(self, left_bottom):

		self.left = left_bottom[0]
		self.bottom = left_bottom[1]

		self.rocks_relative_position = {
			(0, 0),
			(1, 0),
			(2, 0),
			(2, 1),
			(2, 2)
		}

class VerticalLine():

	def __init__(self, left_bottom):

		self.left = left_bottom[0]
		self.bottom = left_bottom[1]

		self.rocks_relative_position = {
			(0, 0),
			(0, 1),
			(0, 2),
			(0, 3)
		}

class Cube():

	def __init__(self, left_bottom):

		self.left = left_bottom[0]
		self.bottom = left_bottom[1]

		self.rocks_relative_position = {
			(0, 0),
			(0, 1),
			(1, 0),
			(1, 1)
		}

def can_go_left(my_map, rock):

	left_rock = rock.left
	bottom_rock = rock.bottom

	for rock_part in rock.rocks_relative_position:
		x_pos = rock_part[0] + left_rock
		y_pos = rock_part[1] + bottom_rock

		if x_pos - 1 < 0:
			return False

		if (x_pos - 1, y_pos) in my_map:
			return False

	return True

def can_go_right(my_map, rock, width):

	left_rock = rock.left
	bottom_rock = rock.bottom

	for rock_part in rock.rocks_relative_position:
		x_pos = rock_part[0] + left_rock
		y_pos = rock_part[1] + bottom_rock

		if x_pos + 1 >= width:
			return False

		if (x_pos + 1, y_pos) in my_map:
			return False

	return True

def can_go_down(my_map, rock):
	left_rock = rock.left
	bottom_rock = rock.bottom

	for rock_part in rock.rocks_relative_position:
		x_pos = rock_part[0] + left_rock
		y_pos = rock_part[1] + bottom_rock

		if y_pos - 1 < 1:
			return False

		if (x_pos, y_pos - 1) in my_map:
			return False

	return True

def rock_rest(my_map, rock):
	left_rock = rock.left
	bottom_rock = rock.bottom

	for rock_part in rock.rocks_relative_position:
		x_pos = rock_part[0] + left_rock
		y_pos = rock_part[1] + bottom_rock

		my_map[(x_pos, y_pos)] = ROCK_REST

def update_highest_rock(highest_rock, rock):
	result = highest_rock

	bottom_rock = rock.bottom

	for rock_part in rock.rocks_relative_position:
		y_pos = rock_part[1] + bottom_rock

		result = max(result, y_pos)

	return result

def is_flat(my_map, highest_rock):

	for i in range(width):
		if not((i, highest_rock) in my_map):
			return False

	return True

order_rocks_class = [HorizontalLine, Cross, LShape, VerticalLine, Cube]

width = 7
highest_rock = 0
rock_class_index = 0
jet_index = 0
my_map = {}

# for i in range(7):
# 	my_map[(i, 0)] = ROCK_REST

rock_fallen = 0
rock_falling = order_rocks_class[rock_class_index]((2, highest_rock + 4))

save_highest_rock = highest_rock
save_jet_index = jet_index

while rock_fallen < 2022:

	### Jet of gas

	jet = data[jet_index]
	jet_index = (jet_index + 1) % len(data)

	if jet == ">":
		if can_go_right(my_map, rock_falling, width):
			rock_falling.left += 1

	elif jet == "<":
		if can_go_left(my_map, rock_falling):
			rock_falling.left -= 1

	else:
		print("should not happen")

	### Rock fall

	if can_go_down(my_map, rock_falling):
		rock_falling.bottom -= 1

	else:
		rock_rest(my_map, rock_falling)
		rock_fallen += 1

		highest_rock = update_highest_rock(highest_rock, rock_falling)

		rock_class_index = (rock_class_index + 1) % len(order_rocks_class)

		rock_falling = order_rocks_class[rock_class_index]((2, highest_rock + 4))

print(highest_rock)