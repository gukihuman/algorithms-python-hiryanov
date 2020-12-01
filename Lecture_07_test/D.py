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

my_list = get_list()
print(greatest_even(my_list))