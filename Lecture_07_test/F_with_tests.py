def nod(big, small):
	"""Return the greatest common divisor of two numbers."""
	if big < small:
		big, small = small, big
	if big % small == 0:
		return small
	sub = big - small
	big = small
	small = sub
	return nod(big, small)

def test_1(nod):
	print('Test 1: ', end='')
	print('OK' if nod(30, 18) == 6 else 'Fail')

def test_2(nod):
	print('Test 2: ', end='')
	print('OK' if nod(1071, 462) == 21 else 'Fail')

def test_3(nod):
	print('Test 3: ', end='')
	print('OK' if nod(462, 1071) == 21 else 'Fail')

test_1(nod)
test_2(nod)
test_3(nod)