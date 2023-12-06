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

ranges = [Pair_Range(1, 5)]

overlaps = [Pair_Range(2, 2)]

print(remove_overlaps(ranges, overlaps))
