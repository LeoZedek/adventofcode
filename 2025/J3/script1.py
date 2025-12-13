with open('input', 'r') as file:
	data = file.read().splitlines()

result = 0

for bankBatteries in data:
	biggestFirstBattery = max(bankBatteries[:-1])
	biggestSecondBattery = max(bankBatteries[bankBatteries.index(biggestFirstBattery) + 1:])

	result += int(biggestFirstBattery) * 10 + int(biggestSecondBattery)

print(result)