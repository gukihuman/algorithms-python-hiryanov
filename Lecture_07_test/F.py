def nod(big, small):
	"""Return the greatest common divisor of two numbers."""
	if big < small:
		big, small = small, big
	if big % small == 0:
		return small
	sub = big - small
	big = small
	small = sub
	return nod(big, small)

print(nod(int(input()), int(input())))