"""
There is two tasks in one. I guess it's a mistake of the course author, because
there is no information about this in the task discription on the site.
Let's name these two tasks "Option A" and "Option B". The official course
discription on the site is only about the "Option A". But online tests also
need the "Option B". Regardless of it, the problem is solvable. For completing
the tests, first of all, checks the first line. If it has an empty space,
there is an "Option B". Else "Option A". The discription for the options
will follow below.

This task is working with huge data from input.
There is no test for it. Only contest online-test.
"""


def max(number_1, number_2):
    """
    Finds a maximum number of two input numbers.

    :param number_1: a first number
    :param number_2: a second number
    :return: a maximum number of two input numbers.
    """

    if number_1 > number_2:
        return number_1
    return number_2


def min(number_1, number_2):
    """
    Finds a minimum number of two input numbers.

    :param number_1: a first number
    :param number_2: a second number
    :return: a mimimum number of two input numbers.
    """

    if number_1 < number_2:
        return number_1
    return number_2


# Sets an "Option A" variable to "True" by default.
option_A = True

# Catches a first line.
first_line = str(input())

# Checks the first line for an empty space.
# If there is an empty space, an "Option B" is on.
for i in first_line:

    # Checks a symbol if it's an empty space or not.
    if i == " ":

        # Sets the "option A" variable to "False". It will be used by
        # the main "if" term for picking the right part of the code.
        option_A = False

        # No need to check the whole line. If an empty space is found,
        # the "Option B" is on for shure. So just breaks the cycle.
        break


"""
Option A:
There is a sequence of integer numbers. The size of the sequence is always
devided by 3 without residue. Find four numbers from the sequence.
First number is a middle number from all numbers of the sequence.
Second number is a maximum number from all numbers of the sequence.
Third number is a minimum number from all numbers of the sequence.
Fourth number is a tricky one and needs an additional explanations.
The sequence is made by triplets. Every triplet contains three numbers.
Find an addition of numbers in a triplet. Then, find the residue of
the devision of the addition by the last number in the triplet.
For example, the addition of 5, 6, 7 is 18. In this case, the residue of
the devision of 18 by 7 is 4. Coming back to the fourth number needed
to find, it's the addition of these residues from all triplets.


Input format:
A sequence of integer numbers. Each one is on a new line. "#" means an end.
A numbers are from 1 to 100.

Output format:
Four numbers in one line separated by an empty space.
First number is a float middle number rounded to three decimal places.
Second number is an integer maximum number.
Third number is an integer minimum number.
Fourth number is an integer number. It's an addition of the residues from
all triplets.
"""

# If "Option A" variable is "True", there is an "Option A".
if option_A:

    # Sets an addition of all numbers in the sequence to 0.
    # It will be used for the middle number calculation.
    sequence_addition = 0

    # Sets a counter of numbers to 0.
    # It will be used for the middle number calculation.
    counter = 0

    # Sets maximum of all numbers in the sequence to 0.
    # Input numbers are from 1 to 100, so any number will be bigger.
    sequence_maximum = 0

    # Sets minimum of all numbers in the sequence to 101.
    # Input numbers are from 1 to 100, so any number will be lesser.
    sequence_minimum = 101

    # Sets an addition of triplet residues to 0.
    residues_addition = 0

    # First checking line already exists. It's the first line.
    # Sets the checking line to the first line.
    checking_line = first_line

    # Starts the cycle while the checking line is not a "#" symbol.
    # The cycle works with a triplet. A first number of the triplet is
    # on the checking line. A second and a third number are getting from
    # input. After all calculations, getting a new checking line from input.
    while checking_line != '#':

        # Sets a triplet by the checking line and two inputs.
        triplet = [int(checking_line), int(input()), int(input())]

        # Adds the all triplet numbers to the sequence addition variable.
        # It will be used for the middle number calculation.
        sequence_addition += triplet[0] + triplet[1] + triplet[2]

        # Adds three to the counter of numbers.
        counter += 3

        # Calculates a maximum number of the triplet.
        triplet_maximum = max(triplet[0], max(triplet[1], triplet[2]))

        # Sets a sequence maximum to triplet maximum, if it's greater.
        if triplet_maximum > sequence_maximum:
            sequence_maximum = triplet_maximum

        # Calculates a minimum number of the first triplet.
        triplet_minimum = min(triplet[0], min(triplet[1], triplet[2]))

        # Sets a sequence minimum to triplet minimum, if it's lesser.
        if triplet_minimum < sequence_minimum:
            sequence_minimum = triplet_minimum

        # Calculates the addition of the triplet numbers.
        # Then calculates a residue of a devision of the addition by
        # the last number in the triplet.
        triplet_residue = (triplet[0] + triplet[1] + triplet[2]) % triplet[2]

        # Adds the triplet residue to the addition of all residues.
        residues_addition += triplet_residue

        # Catches a checking line as a string, it might be a "#" symbol.
        checking_line = str(input())

    # Calculates a middle number and round it to three decimal places.
    middle_number = round(sequence_addition / counter, 3)

    # Prints the answer. It's a string with four numbers.
    print(middle_number, sequence_maximum, sequence_minimum, residues_addition)


"""
Option B:
There is a sequence of numbers. Shift down the sequence by one.
Indexes of every number has to be lesser by 1, except the first.
The first has to be the last.

Input format:
A string with numbers separated by an empty space.

Output format:
A string with numbers separated by an empty space based on
the input string but with bias down by one.
"""

# If "Option A" variable is "False", there is an "Option B".
if not option_A:

    # Splits the first line by an empty space.
    # "First line" variable is a string. "Sequence" is a list.
    sequence = first_line.split()

    # Sets a temporary variable to the first item of the sequence.
    temp = sequence[0]

    # Initialazes a cycle with an amount of iterations equals to the size of
    # the sequence minus one. Substraction by one is needed, becouse the cycle
    # works with two items in each iteration: current index and the second one.
    for i in range(len(sequence) - 1):

        # Sets an item in the sequence to the value of the second item in
        # the sequence. In other words, decreases indexes of every item,
        # except the first one.
        sequence[i] = sequence[i+1]

    # Sets the last item in the sequence to the temporary variable,
    # which is equal to the first item from the sequence before the changes.
    sequence[-1] = temp

    # Prints the answer. It's the changed sequence.
    print(*sequence)
