def digits_sum(number):
    """
    Finds the sum of every digit in a three-digit number.

    :param number: a three-digit number
    :return: the sum of every digit in the number
    """

    # Transforms the number from integer-type to string-type.
    number = str(number)

    # Adds every digit and returns the amount
    return int(number[0]) + int(number[1]) + int(number[2])


"""
Input format:
A three-digit number.

Output format:
The number representing the sum of every digit in the input number.
"""

# Catches the number from input.
number = int(input())

# Uses the function to find the sum of every digit in the input number.
answer = digits_sum(number)

# Print the answer.
print(answer)
