"""
Finds the maximum number in a sequence. The sequence is getting from input.
It is done when input number is 0. The input numbers are greater then zero.
"""

# Creates a variable for a maximum number.
max_number = 0

# Catches the first number.
number = int(input())

# While the input number is not zero, checks if it is the maximum number.
# If it is, saves it.
while number != 0:

	# Saves the number as maximum number if it is greater then
	# the existing maximum number.
	if number > max_number:
		max_number = number

	# Catches the new number.
	number = int(input())

# Prints the value of the maximum number.
print(max_number)