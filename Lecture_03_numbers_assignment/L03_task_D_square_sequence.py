def square_sequence(max_square):
	"""
	Returns a sequence of squares of integers in ascending order up to
	the case where the square is greater or equal to the maximum square.
	The maximum square is getting from input of the function.
	The maximum square must be greater then zero.

	:param max_square: a number of the maximum square
	:return: the sequence of squares of integers
	"""

	# Creates a list for squares.
	squares = []

	# Creates a variable for the first square.
	square = 1

	# Creates a variable for the first integer.
	integer = 1

	# Starts a cycle of creating a sequence of squares while the square is
	# lesser or equal to the max_square.
	while square <= max_square:

		# Appends the square to the square-list.
		squares.append(square)

		# Sets a next integer.
		integer += 1

		# Sets a square of the integer.
		square = integer ** 2

	# Returns the sequence of the squares.
	return squares