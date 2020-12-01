def ride_pos(spec):
	"""
	Returns possibility of the riding using the specifications
	of a car and our supply and characteristics of a road

	spec(
	weight of the car,		# 0
	height of the platform,	# 1
	weight of the piano,		# 2
	height of the piano,		# 3
	weight of the refrigerator,		# 4
	height of the refrigerator,		# 5
	maximum weight on a road to institute	# 6
	maximum height on a road to hostel		# 7
	)

	"""

	def check_institute():
		if  weight <= spec[6]:
			return True
		return False

	def check_hostel():
		if height <= spec[7]:
			return True
		return False

	#  specifications at the start
	weight = spec[0] + spec[2] + spec[4]
	piano_height = spec[1] + spec[3]
	ref_height = spec[1] + spec[5]
	if spec[3] > spec[5]:
		height = piano_height
	else:
		height = ref_height

	#  ride
	if check_hostel():
		weight -= spec[4]
		if check_institute():
			return 'YES'
		return 'NO'
	else:
		if check_institute():
			height = ref_height
			if check_hostel():
				return 'YES'
			return 'NO'
		return 'NO'

def test_ride_pos_1(test_func):
	print("Test 1: ", end='')
	list_spec = (1,1,5,10,5,10,10,10)
	print('OK' if test_func(list_spec) == 'NO' else 'Fail')

def test_ride_pos_2(test_func):
	print("Test 2: ", end='')
	list_spec = (1,1,5,10,5,10,11,11)
	print('OK' if test_func(list_spec) == 'YES' else 'Fail')

def test_ride_pos_3(test_func):
	print("Test 3: ", end='')
	list_spec = (1,1,3,5,6,10,4,11)
	print('OK' if test_func(list_spec) == 'YES' else 'Fail')

def test_ride_pos_4(test_func):
	print("Test 4: ", end='')
	list_spec = (1,1,3,15,5,10,10,12)
	print('OK' if test_func(list_spec) == 'YES' else 'Fail')

test_ride_pos_1(ride_pos)
test_ride_pos_2(ride_pos)
test_ride_pos_3(ride_pos)
test_ride_pos_4(ride_pos)