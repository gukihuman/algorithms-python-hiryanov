"""
Finds how many of numbers in a sequence are equal to the maximum number in
the sequence. The sequence is getting from input. It is done when
input number is 0. The input numbers are greater then zero.

This task is working with huge data from input.  
There is no test for it. Only contest online-test.
"""

# Input format:
# A sequence of numbers. Each one is on a new line. "0" means an end.

# Output format:
# A number which is an amount of the input numbers which are equal to
# the max number in the sequence.


# Creates a variable for a maximum number.
max_number = 0

# Creates a variable for a counter of numbers.
counter = 0

# Catches the first number.
number = int(input())

# While the input number is not zero, checks if it is the maximum number.
# If it is, saves it. Counts how many numbers is equal to the maximum number.
while number != 0:

    # Saves the number as maximum number if it is greater then
    # the existing maximum number. Also sets the counter to 1.
    if number > max_number:
        max_number = number
        counter = 1

    # Increases the counter by 1 if the number is equal to maximum number.
    elif number == max_number:
        counter += 1

    # Catches the new number.
    number = int(input())

# Prints the value of the counter of the numbers equals to the maximum number.
print(counter)
