"""
Finds the maximum number in a sequence. The sequence is getting from input.
It is done when input number is 0. The input numbers are greater then zero.

This task is working with huge data from input.  
There is no test for it. Only contest online-test.
"""

# Input format:
# A sequence of numbers. Each one is on a new line. "0" means an end.

# Output format:
# A number which is the max input number.


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
