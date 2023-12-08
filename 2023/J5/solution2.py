class Pair_Range:
	def __init__(self, start, value, ending_value = False):
		self.start = start
		if ending_value:
			self.end = value
			self.length = self.end - self.start + 1
		else:
			self.length = value
			self.end = start + self.length - 1

	def __repr__(self):
		return "[" + str(self.start) + ", " + str(self.end) + "]"

class Map:
	def __init__(self, pair_range_source, pair_range_destination):
		self.pair_range_source = pair_range_source
		self.pair_range_destination = pair_range_destination

	def map(self, source):
		if type(source) == int:
			return self.pair_range_destination.start + source - pair_range_source.start

		elif type(source) == type(Pair_Range(1, 2)):
			return Pair_Range(self.pair_range_destination.start + source.start - self.pair_range_source.start, source.length)

	def __repr__(self):
		return "source :" + self.pair_range_source.__repr__() + "\ndestination :" + self.pair_range_destination.__repr__()

def find_overlap(range1, range2):
	if range1.start > range2.end or range2.start > range1.end:
		return None

	return Pair_Range(max(range1.start, range2.start), min(range1.end, range2.end), ending_value = True)

def remove_overlap(_range, overlap):

	if overlap.start == _range.start and overlap.end == _range.end:
		return []

	if overlap.end == _range.end:
		return [Pair_Range(_range.start, overlap.start - 1, ending_value = True)]

	if overlap.start == _range.start:
		return [Pair_Range(overlap.end + 1, _range.end, ending_value = True)]

	return [Pair_Range(_range.start, overlap.start - 1, ending_value = True), Pair_Range(overlap.end + 1, _range.end, ending_value = True)]

def is_overlap(range1, range2):
	return not(range1.start > range2.end or range1.end < range2.start)

def remove_overlaps(ranges, overlaps):

	for overlap in overlaps:

		temp = []

		for _range in ranges:
			if is_overlap(_range, overlap):
				without_overlap = remove_overlap(_range, overlap)
				temp += without_overlap
			else:
				temp.append(_range)

		ranges = temp

	return ranges


def transform(maps, source_ranges):
	result = []

	unmap_values = source_ranges

	overlap_found = []

	for _map in maps:

		for unmap_value in unmap_values:

			overlap = find_overlap(_map.pair_range_source, unmap_value)

			if not(overlap is None):
				result.append(_map.map(overlap))
				overlap_found.append(overlap)

	for overlap in overlap_found:

		temp = []

		for unmap_value in unmap_values:
			if is_overlap(unmap_value, overlap):
				without_overlap = remove_overlap(unmap_value, overlap)

				temp += without_overlap
			else:
				temp.append(unmap_value)

		unmap_values = temp

	return result + unmap_values

with open("input", "r") as file:
	data = file.readlines()

seeds = list(map(int, data[0].split(": ")[1].split()))

seeds_range = []

for i in range(0, len(seeds), 2):
	seeds_range.append(Pair_Range(seeds[i], seeds[i + 1]))

i = 3

mapped_values = []

while i < len(data):

	mapped_value = []

	while i < len(data) and data[i] != "\n":

		destination_start, source_start, length = list(map(int, data[i].split()))

		mapped_value.append(Map(Pair_Range(source_start, length), Pair_Range(destination_start, length)))
		i += 1

	mapped_values.append(mapped_value)

	i += 2

min_location = -1

source_ranges = seeds_range

for i in range(len(mapped_values)):
	maps = mapped_values[i]
	source_ranges = transform(maps, source_ranges)

print(min(source_ranges, key = lambda x: x.start).start)
