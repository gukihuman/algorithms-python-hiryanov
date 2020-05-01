"""
There is a sequence of "0" and "1". Find a max amount of the "1" in a row.

This task is working with huge data from input.
There is no test for it. Only contest online-test.

Input format:
First line is a number which is a size of following sequence.
The size of the sequence is from 1 to 10000.
Then a sequence of numbers: "0" or "1". Each one is on a new line.

Output format:
A number which is a max amount of the "1" in a row.
"""

# Sets a current amount of "1" in a row to 0 at the beginning.
current_amount = 0

# Sets a max amount of "1" in a row to 0 at the beginning.
max_amount = 0

# Catches the size of the sequence.
size = int(input())

# Initializes a cycle for an amount of iterations equals to
# the size of the secquence.
for i in range(size):

    # Catches a number.
    number = int(input())

    # Increases by 1 a current amount of "1" in a row if the number is "1".
    # Else resets it to zero.
    if number == 1:
        current_amount += 1
    else:
        current_amount = 0

    # Sets a max amount of "1" in a row to the current amount if it's greater.
    if current_amount > max_amount:
        max_amount = current_amount

# Prints the max amount.
print(max_amount)
