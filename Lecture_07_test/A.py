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

specifications = [0] * 8
for x in range(8):
	specifications[x] = int(input())

print(ride_pos(specifications))