def biggest(a, b):
	if a > b:
		return a
	return b

def triangle_type(s1, s2, s3):
	"""Return a type of triangle by it's sides."""

	# find the biggest side and define others
	c = biggest(biggest(s1, s2), s3)
	if c == s1:
		a, b = s2, s3
	elif c == s2:
		a, b = s1, s3
	else: #  c == s3
		a, b = s1, s2

	# check correctness
	if c >= a + b:
		return 'impossible'

	# find type
	sq_c = c ** 2
	sq_a_b = a ** 2 + (b ** 2)
	if sq_c == sq_a_b:
		return 'right'
	elif sq_c < sq_a_b:
		return 'acute'
	return 'obtuse' #  sq_c > sq_a_b

def test_1(function):
	print('Test 1: ', end='')
	print('OK' if function(3,4,5) == 'right' else 'Fail')

def test_2(function):
	print('Test 2: ', end='')
	print('OK' if function(6,4,7) == 'acute' else 'Fail')

def test_3(function):
	print('Test 3: ', end='')
	print('OK' if function(6,4,8) == 'obtuse' else 'Fail')

def test_4(function):
	print('Test 4: ', end='')
	print('OK' if function(6,11,4) == 'impossible' else 'Fail')

test_1(triangle_type)
test_2(triangle_type)
test_3(triangle_type)
test_4(triangle_type)