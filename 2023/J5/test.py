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
	if range1.start > range2.end or range2.end < range1.start:
		return None

	return Pair_Range(max(range1.start, range2.start), min(range1.end, range2.end), ending_value= True)

def remove_overlap(_range, overlap):

	if overlap.start == _range.start and overlap.end == _range.end:
		return []

	if overlap.end == _range.end:
		return [Pair_Range(_range.start, overlap.start - 1, ending_value = True)]

	if overlap.start == _range.start:
		return [Pair_Range(overlap.end + 1, _range.end, ending_value = True)]

	return [Pair_Range(_range.start, overlap.start - 1, ending_value = True), Pair_Range(overlap.end + 1, _range.end, ending_value = True)]

def is_overlap(range1, range2):
	return not(range1.start > range2.end or range2.end < range1.start)

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

	# print(source_ranges)

	# print(overlap_found)

	# print(maps)

	# assert(1 != 1)

	for overlap in overlap_found:

		temp = []

		for unmap_value in unmap_values:
			if is_overlap(unmap_value, overlap):
				without_overlap = remove_overlap(unmap_value, overlap)
				temp += without_overlap
			else:
				temp.append(unmap_value)

		unmap_values = temp

	print("coucou")

	return result + unmap_values

range1 = Pair_Range(55, 67, ending_value = True)

range2 = Pair_Range(79, 92, ending_value = True)

print(range1)
print(range2)

print(is_overlap(range1, range2))

overlap = find_overlap(range2, range1)

print(overlap)

print(remove_overlap(range1, overlap))