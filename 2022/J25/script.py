with open("input") as f:
	data = list(map(lambda x : x.split('\n')[0], f.readlines()))

digitsValues = {
	"=" : -2,
	"-" : -1,
	"0" : 0,
	"1" : 1,
	"2" : 2
}

digits_order = ["=", "-", "0", "1", "2"]

base = 5

def SNAFUtoDecimal(SNAFUcode, base, digitsValues):

	length = len(SNAFUcode)

	decimal_value = 0

	for i in range(length):
		decimal_value += digitsValues[SNAFUcode[i]] * base**(length - 1 - i)

	return decimal_value

def decimalToBase(decimal_code, base):

	result = ""

	while decimal_code // base != 0:
		result = str(decimal_code % base) + result
		decimal_code = decimal_code // base

	result = str(decimal_code) + result

	return result

def base_to_SNAFU(code, base, digits_order):

	result = list(code)

	length = len(result)

	for i in range(length - 1, -1, -1):

		if int(result[i]) > base // 2:

			index_new_digits = int(result[i]) - (base // 2) - 1

			result[i] = digits_order[index_new_digits]

			if i > 0:
				result[i - 1] = str(int(result[i - 1]) + 1)

			else:
				result.insert(0, "1")

	return "".join(result)

def decimal_to_SNAFY(code, base, digits_order):

	return base_to_SNAFU(decimalToBase(code, base), base, digits_order)

res_decimal = 0

for string_data in data:

	res_decimal += SNAFUtoDecimal(string_data, base, digitsValues)


print(decimal_to_SNAFY(res_decimal, base, digits_order))