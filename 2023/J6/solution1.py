with open("input", "r") as file:

	data = file.readlines()


times = list(map(int, data[0].split(":")[1].strip().split()))

distances = list(map(int, data[1].split(":")[1].strip().split()))

ways_to_beat_record = []

for i in range(len(times)):

	time = times[i]
	distance = distances[i]

	way_to_beat_record = 0

	for hold_time in range(time + 1):
		if hold_time * (time - hold_time) > distance:
			way_to_beat_record += 1

	ways_to_beat_record.append(way_to_beat_record)

result = 1

for number in ways_to_beat_record:
	result *= number

print(result)