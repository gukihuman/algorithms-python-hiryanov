def logarithm(number):
    """
    Finds the base 2 logarithm of the input number. Rounded up for integrity.
    In other words, finds the power of 2 where the result is greater
    then the input number. The input number must be greater then zero.

    :param number: a number
    :return: the base 2 logarithm of the number
    """

    # Creates a variable for the number which is lesser or equal to 2.
    power = 1

    # Divides the number by 2 while the number is lesser or equal to 2.
    # Counts every iteration and adds it to the power variable.
    while number > 2:
        number /= 2
        power += 1

    # Returns the power of 2 where the result is greater then the input number.
    return power

# Input format:
# A number.

# Output format:
# A number of the power of the 2 where the result is greater then
# the input number.

# Catches the number from input.
number = int(input())

# Uses the function to find the base 2 logarithm.
answer = logarithm(number)

# Prints the answer.
print(answer)