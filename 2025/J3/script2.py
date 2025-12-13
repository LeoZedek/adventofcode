with open('input', 'r') as file:
	data = file.read().splitlines()

result = 0

for bankBatteries in data:
	voltage = 0
	for i in range(11, -1, -1):
		biggestBattery = max(bankBatteries[:len(bankBatteries)-i])
		bankBatteries = bankBatteries[bankBatteries.index(biggestBattery) + 1:]
		voltage = voltage * 10 + int(biggestBattery)

	result += voltage

print(result)