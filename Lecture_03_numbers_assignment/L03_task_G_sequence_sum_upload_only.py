"""
Finds a sum of numbers in a sequence. The sequence is getting from input.
It is done when input number is 0.
"""

# Creates a variable for a sum of numbers.
sum = 0

# Catches the first number.
number = int(input())

# While the input number is not zero, counts the input numbers.
while number != 0:

	# Increases the counter by 1.
	sum += number

	# Catches the new number.
	number = int(input())

# Prints the value of counter.
print(sum)