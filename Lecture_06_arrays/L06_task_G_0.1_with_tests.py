import math

def power(string, integer):
	"""Returns a string from the input string which is raised to
	the power getting also by input. If there is no answer returns
	'NO SOLUTION'"""
	A = list()
	if integer == 0:
		return 0
	elif integer > 0:
		for k in range(integer):
			A += string
		return ''.join(A)
	else:
		first = string[0]
		pattern = list()
		pattern += first
		count = 0
		for k in range(len(string)):
			if string[k] == first:
				count += 1
		if count > 1:
			k = 1
			while string[k] != first:
				pattern += string[k]
				k += 1
			size = len(pattern) * (math.fabs(integer) - 1)
			string = string[:-int(size)]
			return ''.join(string)
		else:
			return 'NO SOLUTION'

def test_1(power_algorithm):
	print('Test 1: ', end='')
	print('OK' if power_algorithm('abc', 3) == 'abcabcabc' else 'Fail')

def test_2(power_algorithm):
	print('Test 2: ', end='')
	print('OK' if power_algorithm('abcdabcd', -2) == 'abcd' else 'Fail')

def test_3(power_algorithm):
	print('Test 3: ', end='')
	print('OK' if power_algorithm('abcd', -4) == 'NO SOLUTION' else 'Fail')

test_1(power)
test_2(power)
test_3(power)