def get_list():
	"""Return a list of numbers from input. The symbol of the end is 0."""
	x = None
	my_list = list()
	while x != 0:
		x = int(input())
		my_list.append(x)
	my_list = my_list[:-1]
	return my_list

def greatest_even(my_list):
	"""Return the greatest even number from a list."""
	even = []
	for i in range(len(my_list)):
		if my_list[i] % 2 == 0:
			even.append(my_list[i])
	if even == []:
		return 0
	n = even[0]
	for i in range(1, len(even)):
		if n < even[i]:
			n = even[i]
	return n


# Tests:

def test_get_list_1(get_list):
	print("Test get_list 1:\nPlease enter 3, 5, 6, 0:")
	my_list = get_list()
	print(my_list)
	print('OK' if my_list == [3, 5, 6] else 'Fail')

def test_greatest_even_1(greatest_even):
	print('Test 1: ', end='')
	print('OK' if greatest_even([1, 2, 4, 7, 4]) == 4 else 'Fail')

def test_greatest_even_2(greatest_even):
	print('Test 2: ', end='')
	print('OK' if greatest_even([1, 3, 5]) == 0 else 'Fail')

#test_get_list_1(get_list)
test_greatest_even_1(greatest_even)
test_greatest_even_2(greatest_even)