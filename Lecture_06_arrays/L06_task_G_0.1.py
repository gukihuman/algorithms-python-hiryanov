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

string = str(input())
integer = int(input())
print(power(string, integer))