import math


def bank_deposit(deposit, percent, target):
    """
    There is a bank deposit. It increases by percents every year.
    The payment is rounded down to two decimal places.
    Find an amount of years to reach the target deposit.

    :param deposit: a bank deposit
    :param percent: a year percent
    :param target: a target bank deposit
    :return: an amount of years
    """

    # Sets an amount of years to 0 at the beginning.
    year = 0

    # Initializes a cycle for one year while a starting deposit is lesser then
    # a target deposit.
    while deposit < target:

        # Adds to deposit a payment by percents.
        deposit += deposit * (percent/100)

        # Rounds the deposit down to two decimal places.
        deposit *= 100
        deposit = math.floor(deposit)
        deposit /= 100

        # Increases an amount of years.
        year += 1

    # Returns an amount of years when a starting deposit is bigger or
    # equal to a target deposit.
    return year


"""
Input format:
A string with three digits and space between them. A first digit is
a bank deposit. The second digit is a year percent of the deposit.
The third digit is a target deposit.

Output format:
A number of years to reach the target deposit.
"""

# Catches the values from input.
input_string = str(input()).split()
deposit = int(input_string[0])
percent = int(input_string[1])
target = int(input_string[2])

# Uses the function to find an amount of years to reach the target deposit.
answer = bank_deposit(deposit, percent, target)

# Print the answer.
print(answer)
