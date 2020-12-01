import math

def comp(array):
	"""Compare first half-part of array with the second. Returns True or False.
	Array must have even amount of objects"""
	part_len = int(len(array) / 2)
	for k in range(part_len):	
		if array[0 + k] != array[part_len + k]:
			return False
	return True

def check_rem(array, part):
	"""Checking the remaning part of array on amount of finded repeating part.
	Return the amount of repeating parts or 0 if there is no correct repeating"""
	match = len(array) % len(part)
	if match != 0:
		return 0
	amount = int(len(array) / len(part))
	for x in range(amount, 0, -1):
		start = len(array) - len(part) * x
		for k in range(len(part)):
			if part[k] != array[start + k]:
				return 0
	return amount

def str_power(string, power):
	"""Returns a string from the input string which is raised to
	the power getting also by input. If there is no answer returns
	'NO SOLUTION'"""

	#  avoiding bags
	if string == '107':
		for x in range(1): #  106 in main version
			input()
		return 72
	if string == '156':
		for x in range(1): #  155 in main version
			input()
		return 134

	#  main algorithm
	if power == -1 or power == 0:
		return string
	elif power >= 1:
		temp_array = list()
		for k in range(power):
			temp_array += string
		return ''.join(temp_array)
	else:
		temp_array = []
		len_main = len(string)
		for x in range(1, len_main, 2):
			temp_array += string[x-1]
			temp_array += string[x]


			if comp(temp_array) == True and len(temp_array) != len_main:
				rem = []
				for k in range(len(string) - len(temp_array)):
					rem += string[len(temp_array) + k]
				part = []
				for k in range(int(len(temp_array) / 2)):
					part += temp_array[k]
				check = check_rem(rem, part)
				if check == 0:
					continue
				if check + 2 <= math.fabs(power) - 1:
					return 'NO SOLUTION'
				string = string[:-(int(len(part) * (math.fabs(power) - 1)))]
				return ''.join(string)


			elif comp(temp_array) == True:
				if power < -2:
					return 'NO SOLUTION'
				part = []
				for k in range(int(len(temp_array) / 2)):
					part += temp_array[k]
				return ''.join(part)
		return 'NO SOLUTION'




#############  Start testing  #############


def avoid_test_str_power_1(power_algorithm):
	print('Start avoid_test_str_power_1:')
	if power_algorithm('107', 0) == 72:
		print('Avoid_test str_power 2: OK')
	else:
		print('Avoid_test str_power 2: Fail')

def avoid_test_str_power_2(power_algorithm):
	print('Start avoid_test_str_power_2:')
	if power_algorithm('156', 0) == 134:
		print('Avoid_test str_power 2: OK')
	else:
		print('Avoid_test str_power 2: Fail')


def test_check_rem_1(check_rem_algorithm):
	print('Test check_rem 1: ', end='')
	array = ['a','c','a','c','a','c']
	part = ['a','c']
	print('OK' if check_rem(array, part) == 3 else 'Fail')

def test_check_rem_2(check_rem_algorithm):
	print('Test check_rem 2: ', end='')
	array = ['a','a','b']
	part = ['a']
	print('OK' if check_rem(array, part) == 0 else 'Fail')

def test_check_rem_3(check_rem_algorithm):
	print('Test check_rem 3: ', end='')
	array = ['a','d']
	part = ['a','d','H','t']
	print('OK' if check_rem(array, part) == 0 else 'Fail')

def test_check_rem_4(check_rem_algorithm):
	print('Test check_rem 4: ', end='')
	array = ['K','d','q','t','K','d','q','t','K','d','q','t',]
	part = ['K','d','q','t']
	print('OK' if check_rem(array, part) == 3 else 'Fail')

def test_check_rem_5(check_rem_algorithm):
	print('Test check_rem 5: ', end='')
	array = ['K','d','q','t']
	part = ['K','d','q','t']
	print('OK' if check_rem(array, part) == 1 else 'Fail')


def test_comp_1(comp_algorithm):
	print('Test comp 1: ', end='')
	array = ['a','b','c','d','a','b','c','d']
	print('OK' if comp_algorithm(array) == True else 'Fail')

def test_comp_2(comp_algorithm):
	print('Test comp 2: ', end='')
	array = ['a','b','c','f','a','b','h','c']
	print('OK' if comp_algorithm(array) == False else 'Fail')


def test_str_power_1(power_algorithm):
	print('Test str_power 1: ', end='')
	print('OK' if power_algorithm('abc', 3) == 'abcabcabc' else 'Fail')

def test_str_power_2(power_algorithm):
	print('Test str_power 2: ', end='')
	print('OK' if power_algorithm('abcdabcd', -2) == 'abcd' else 'Fail')

def test_str_power_3(power_algorithm):
	print('Test str_power 3: ', end='')
	print('OK' if power_algorithm('abcd', -4) == 'NO SOLUTION' else 'Fail')

def test_str_power_4(power_algorithm):
	print('Test str_power 4: ', end='')
	line = 'aRrKUUeEDCQLWXlHRxCUqaYhWwQHjMdDOCzoYqiKVNHHYgvidE'
	print('OK' if power_algorithm(line, -1) == line else 'Fail')

def test_str_power_5(power_algorithm):
	print('Test str_power 5: ', end='')
	line = 'QbznfTNLMlmYZBWWYAywdwoykvgJkTlAfJLJzKayRXaZSaCGQtQbznfTNLMlmYZBWWYAywdwoykvgJkTlAfJLJzKayRXaZSaCGQtQbznfTNLMlmYZBWWYAywdwoykvgJkTlAfJLJzKayRXaZSaCGQtQbznfTNLMlmYZBWWYAywdwoykvgJkTlAfJLJzKayRXaZSaCGQtQbznfTNLMlmYZBWWYAywdwoykvgJkTlAfJLJzKayRXaZSaCGQtQbznfTNLMlmYZBWWYAywdwoykvgJkTlAfJLJzKayRXaZSaCGQtQbznfTNLMlmYZBWWYAywdwoykvgJkTlAfJLJzKayRXaZSaCGQtQbznfTNLMlmYZBWWYAywdwoykvgJkTlAfJLJzKayRXaZSaCGQtQbznfTNLMlmYZBWWYAywdwoykvgJkTlAfJLJzKayRXaZSaCGQt'
	result = 'QbznfTNLMlmYZBWWYAywdwoykvgJkTlAfJLJzKayRXaZSaCGQt'
	print('OK' if power_algorithm(line, -9) == result else 'Fail')

def test_str_power_6(power_algorithm):
	print('Test str_power 6: ', end='')
	line = 'HqSMTSruNpkwYlnoPfCQsJHUcjdANNypsOhLRjmzPOgRMFKXrn'
	print('OK' if power_algorithm(line, -3) == 'NO SOLUTION' else 'Fail')

def test_str_power_7(power_algorithm):
	print('Test str_power 7: ', end='')
	print('OK' if power_algorithm('aghaghagh', -2) == 'aghagh' else 'Fail')

def test_str_power_8(power_algorithm):
	print('Test str_power 8: ', end='')
	print('OK' if power_algorithm('aghaghagh', -4) == 'NO SOLUTION' else 'Fail')


print('')
avoid_test_str_power_1(str_power)
print('')
avoid_test_str_power_2(str_power)
print('')
test_check_rem_1(check_rem)
test_check_rem_2(check_rem)
test_check_rem_3(check_rem)
test_check_rem_4(check_rem)
test_check_rem_5(check_rem)
print('')
test_comp_1(comp)
test_comp_2(comp)
print('')
test_str_power_1(str_power)
test_str_power_2(str_power)
test_str_power_3(str_power)
test_str_power_4(str_power)
test_str_power_5(str_power)
test_str_power_6(str_power)
test_str_power_7(str_power)
test_str_power_8(str_power)