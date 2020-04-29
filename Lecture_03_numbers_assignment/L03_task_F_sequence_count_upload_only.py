"""
Counts numbers in a sequence. The sequence is getting from input.
Counting is done when input number is 0.

This task is working with huge data from input.  
There is no test for it. Only contest online-test.
"""

# Input format:
# A sequence of numbers. Each one is on a new line. "0" means an end.

# Output format:
# A number which is an amount of the input numbers.


# Creates a variable for a counter of numbers.
counter = 0

# Catches the first number.
number = int(input())

# While the input number is not zero, counts the input numbers.
while number != 0:

    # Increases the counter by 1.
    counter += 1

    # Catches the new number.
    number = int(input())

# Prints the value of counter.
print(counter)
