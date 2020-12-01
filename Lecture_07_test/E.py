def my_sum(my_list):
	amount = 0
	for i in range(len(my_list)):
		amount += my_list[i]
	return amount

def three_seq(my_max):
	"""Return the index of threebonacci number which is
	closest greater to input."""
	my_list = [0, 0, 1]
	temp_list = [0, 0, 1]
	new = 1
	index = 2
	while my_max >= new:
		new = my_sum(temp_list)
		my_list.append(new)
		temp_list.append(new)
		temp_list.pop(0)
		index += 1
	return index

my_max = int(input())
print(three_seq(my_max))