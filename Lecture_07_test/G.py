def get_list():
	"""Return the list using firts unput as a length of the list
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

my_list = get_list()
print(often(my_list))