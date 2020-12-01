def get_list():
	"""Return a list of numbers from input. The symbol of the end is 0."""
	x = None
	A_list = list()
	while x != 0:
		x = int(input())
		A_list.append(x)
	A_list = A_list[:-1]
	return A_list

def average(A_list):
	"""Find an average number from list of numbers. Rounding for 2 after comma."""
	full_sum = 0
	for k in range(len(A_list)):
		full_sum += A_list[k]
	return round(full_sum / len(A_list), 2)

def test_get_list_1(get_list):
	print("Test get_list 1:\nPlease enter 3, 5, 6, 0:")
	A_list = get_list()
	print(A_list)
	print('OK' if A_list == [3, 5, 6] else 'Fail')

def test_average_1(average):
	print("Test average 1: ", end="")
	A_list = [4, 8, 5]
	print('OK' if average(A_list) == 5.67 else 'Fail')

test_get_list_1(get_list)
test_average_1(average)