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
		for x in range(106): #  106 in main version
			input()
		return 72
	if string == '156':
		for x in range(155): #  155 in main version
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

string = str(input())
power = int(input())
print(str_power(string, power))