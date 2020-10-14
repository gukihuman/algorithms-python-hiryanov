"""
Like in the previous task, there is two tasks in one. I guess it's a mistake
of the course author, because there is no information about this in the task
description on the site. Let's name these two tasks "Option A" and "Option B".
The official course description on the site is only about the "Option A".
But online tests also need the "Option B". Regardless of it, the problem is
solvable. For completing the tests, first of all, checks the first input line.
If it is a big number, greater then a 1000, there is an "Option B".
Else "Option A". The description for the options will follow below.

This task is working with huge data from input.
There is no test for it. Only contest online-test.
"""


# Sets an "Option A" variable to "True" by default.
option_A = True

# Catches a first line.
first_line = int(input())

# Checks the first line.
# If it's greater then a 1000, an "Option B" is on.
if first_line > 1000:

    # Sets the "option A" variable to "False". It will be used by
    # the main "if" term for picking the right part of the code.
    option_A = False


"""
Option A:
There are the assessments of the students. It is known, how many students are.
An amount of the assessments may vary. Find a sum of the assessments for each
student. Sort students by the sum of their assessments in reverse order. Then,
sort the assessments of each student in reverse order. Sums are not needed
to be printed. Print out only assessments as it's sorted. First, by the sum
of one student in reverse order. Second, by the assessments themselves
in reverse order.

Input format:
The first line is an amount of the students. Then, on each line there is
a student ID and one assessment separated by an empty space. Students may have
a different amount of the assessments. Some students may have no assessments
at all. "#" means the end.

Output format:
One string of numbers with an empty space between them. The numbers are
the assessments of the students, sorted by two terms. The main term is
the assessments' sum of one student in reverse order. The second term is
the assessments themselves in reverse order. There is no special separation
among different students' assessments. The hole string is only numbers with
an empty space between them. For example, just after the assessments
of the best student are ended, the assessments of the second best student
are started with only an empty space between them.

An example of input:
3
2 4
2 2
0 10
2 3
0 3
#

An example of output:
10 3 4 3 2
"""

# If "Option A" variable is "True", there is an "Option A".
if option_A:

    # Creates a big array for upcoming students' assessments.
    # It will contain little arrays with student ID and an assesment.
    assessments = list()

    # Creates a line variable for upcoming lines.
    line = str()

    # Starts the cycle while the line is not a ["#"]. This array with
    # one "#" item appears after "split()" method.
    while line != ["#"]:

        # Catches an input line. Splits it to two numbers. After the splitting
        # the line became a little array with two items. First item is ID of
        # a student. Second item is an assessment of the student.
        line = str(input()).split()

        # Appends the line to the big array of students' assessments.
        assessments.append(line)

    # Deletes the last item from the big array of students' assessments.
    # The item is needless ["#"].
    assessments.pop()

    # Starts the cycle of changing the type of the items in the big array of
    # students' assessments. After this, string items became integer items.
    for i in range(len(assessments)):

        # Changes the type of the both items in the little array.
        # First argument in the square brackets is the index of the big array.
        # Second argument is the index of the little array.
        assessments[i][0] = int(assessments[i][0])
        assessments[i][1] = int(assessments[i][1])

    # Creates an empty list for students' assessments grouped by
    # the student's ID.
    assessments_grouped = list()

    # Fills up the grouped list with an empty arrays which will contain
    # the assessments of just one student. The length of the list is based on
    # the "first_line" variable, which is the amount of the students.
    # The indiсes of the list will be equal to the student's ID.
    for i in range(first_line):
        assessments_grouped.append([])

    # Fills up the grouped list with the assessments of the students.
    # The indices of the grouped list is equal to the student's ID.
    # Each item is an array which contains all the assessments of the student.
    for i in assessments:

        # Gets the student's ID from the first item of the little array in
        # the big array of students' assessments.
        student_id = i[0]

        # Appends the second item of the little array in the big array of
        # students' assessments to the item in the grouped list of the
        # assessments. The index of the item is equal to the student's ID.
        assessments_grouped[student_id].append(i[1])

    # Sorts backwards the grouped list of the students' assessments by the sum
    # of the little array, which is the sum of the assessments for one student.
    # "lambda" function gets the little array and finds the sum of the all
    # it's items. Then the result became the key of the sorting.
    assessments_grouped.sort(key=lambda x: sum(x), reverse=True)

    # Starts the cycle of sorting each item in the grouped list of the
    # assessments.
    for i in range(len(assessments_grouped)):

        # Sorts backwards one item, which is a little array.
        assessments_grouped[i].sort(reverse=True)

    # Starts the cycle of printing the grouped list of the students'
    # assessments without commas. Empty items are not visible.
    for i in assessments_grouped:

        # The end of the printing is just another empty space.
        # This way all the numbers will be printed on the same line.
        print(*i, end=' ')

"""
Option B:
Finds the sequence of prime numbers. A prime number is a natural number
greater than 1 that is not a product of two smaller natural numbers.

Input format:
An integer number, which is upper bound of the sequence of prime numbers.
It is greater then a 1000.

Output format:
A sequence of numbers on one line separated by an empty space.
The last number in the sequence must not be greater then the upper bound
number. It can be equal though.

An example of input:
10000

An example of output (points are reduction, it must not be in the answer):
2 3 5 7 11 13 17 19 23 ...... 9907 9923 9929 9931 9941 9949 9967 9973
"""

# If "Option A" variable is "False", there is an "Option B".
if not option_A:

    # Creates the sequence and fills it up by boolean "True" value.
    # "True" will mean that the number is primal. The length of the sequence
    # is greater by 1 then the upper bound number from the first line.
    # This is necessary because the indices of the sequence will be equal to
    # the numbers and the upper bound number from the first line may be
    # in the sequence too, as the last one.
    sequence = [True] * (first_line + 1)

    # Sets the 0 and 1 to "False". It is know, these numbers aren't primal.
    sequence[0] = sequence[1] = False

    # Starts the cycle in range from 2 to the upper bound number from
    # the first line plus 1. It's necessary to add 1 to the first line,
    # because the number from the first line needs to be uncluded.
    for i in range(2, first_line + 1):

        # Starts the upcoming operation, if the current item of the sequence is
        # "True". It means the number is primal. Just skips non-prime numbers.
        if sequence[i]:

            # Starts the cycle of marking non-prime numbers with "False"
            # based on the current prime number. First, the current number
            # is multiplied by 2. Then the number is going to be greater by
            # the started current prime number as many times, as the length of
            # the sequence allows. In other words, the start of the cycle is
            # the current prime number multiplied by 2 and the step of
            # the cycle is also the current prime number. Every number in
            # the sequence which is stayed with "True" will be primal.
            for k in range(i * 2, first_line + 1, i):
                sequence[k] = False

    # Starts the cycle of printing in range, which is equal to the length of
    # the sequence. It's also the first line number plus 1.
    for i in range(first_line + 1):

        # Starts the printing, if the current item of the sequence is "True".
        # It means the number is primal.
        if sequence[i]:

            # Prints the current number with an empty space in the end.
            # This way all the numbers will be printed on the same line.
            print(i, end=" ")
