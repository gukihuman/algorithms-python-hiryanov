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


#  Tests:

def test_my_sum_1(my_sum):
	print('Test my_sum 1: ', end='')
	print('OK' if my_sum([2, 6, 7, 14]) == 29 else 'Fail')

def test_three_seq_1(three_seq):
	print('Test three_seq 1: ', end='')
	print('OK' if three_seq(0) == 2 else 'Fail')

def test_three_seq_2(three_seq):
	print('Test three_seq 2: ', end='')
	print('OK' if three_seq(10) == 7 else 'Fail')

def test_three_seq_3(three_seq):
	print('Test three_seq 3: ', end='')
	print('OK' if three_seq(13) == 8 else 'Fail')

def test_three_seq_4(three_seq):
	print('Test three_seq 4: ', end='')
	print('OK' if three_seq(1) == 4 else 'Fail')

def test_three_seq_5(three_seq):
	print('Test three_seq 5: ', end='')
	print('OK' if three_seq(2) == 5 else 'Fail')

test_my_sum_1(my_sum)
test_three_seq_1(three_seq)
test_three_seq_2(three_seq)
test_three_seq_3(three_seq)
test_three_seq_4(three_seq)
test_three_seq_5(three_seq)