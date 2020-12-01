def get_list():
	"""Return the list using first input as a length of the list
	and other inputs as elements."""
	length = int(input())
	my_list = []
	for i in range(length):
		my_list.append(int(input()))
	return my_list

def often(my_list):
	"""Return the most often number from a list."""
	hash_table = [0] * 100
	for i in range(len(my_list)):
		n = my_list[i]
		hash_table[n] += 1

	my_max = hash_table[0]
	for i in range(100):
		if my_max < hash_table[i]:
			my_max = hash_table[i]
			n = i
	return n		

#  Tests:

def test_get_list(get_list):
	print("Test get_list 1:\nPlease enter 3, 2, 5, 6:")
	A_list = get_list()
	print(A_list)
	print('OK' if A_list == [2, 5, 6] else 'Fail')

def test_often_1(often):
	print('Test often 1: ', end='')
	print('OK' if often([5, 5, 2, 5]) == 5 else 'Fail')

def test_often_2(often):
	print('Test often 2: ', end='')
	print('OK' if often([7, 7, 7, 5, 5, 2, 7, 4, 5, 4, 7]) == 7 else 'Fail')

#test_get_list(get_list)
test_often_1(often)
test_often_2(often)