def biggest(a, b):
	if a > b:
		return a
	return b

def triangle_type(s1, s2, s3):
	"""Return a type of triangle by it's sides."""

	# find the biggest side and define others
	c = biggest(biggest(s1, s2), s3)
	if c == s1:
		a, b = s2, s3
	elif c == s2:
		a, b = s1, s3
	else: #  c == s3
		a, b = s1, s2

	# check correctness
	if c >= a + b:
		return 'impossible'

	# find type
	sq_c = c ** 2
	sq_a_b = a ** 2 + (b ** 2)
	if sq_c == sq_a_b:
		return 'right'
	elif sq_c < sq_a_b:
		return 'acute'
	return 'obtuse' #  sq_c > sq_a_b

s1 = int(input())
s2 = int(input())
s3 = int(input())
print(triangle_type(s1, s2, s3))