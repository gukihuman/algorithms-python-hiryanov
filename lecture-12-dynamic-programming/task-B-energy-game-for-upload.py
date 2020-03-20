def energy_game(platforms, length=None):
    """
    The hero of a computer game needs to get from one edge of the
    screen to the other, jumping over platforms. In this case, when
    jumping from one platform to the next, the hero leaves | p2 - p1 |
    units of energy, where p1 and p2 are the heights at which these
    platform are located. In addition, the hero has a superpower that
    allows you to jump over the platform, but it takes 3 * | p3 - p1 |
    units of energy. Of course, energy should be spend as economically
    as possible. You know the heights of all platform in order from
    left to right. It is necessary to find what minimum amount of energy
    a hero needs to get from the first platform to the last.

    :param platforms: list of numbers
    :param length: length of the number's list, integer type
    :return: minimum amount of energy to get to the last platform
    """

    # Finds the length of the original number's list if necessary.
    length = length or len(platforms)

    # Insert additional fake platform in the beginning of
    # the platforms' list. It will be used for calculate
    # first jump to second platform.
    platforms.insert(0, float('inf'))

    # Creates the list which saves the minimal amount of energy
    # for each platform. It uses infinite value for the additional
    # fake platform and 0 value for the first one.
    summary = [float('inf'), 0]

    # Finds the minimal amount of energy for each platform
    # starting from second which is in 2 index, because of
    # the fake platform.
    for i in range(2, length + 1):

        # Finds the difference between the height of target platform and
        # the previous. It is necessary to find which is higher and
        # which is lower.
        if platforms[i] is max(platforms[i], platforms[i - 1]):
            higher = platforms[i]
            lower = platforms[i - 1]
        else: # platforms[i - 1] is max(platforms[i], platforms[i - 1]):
            higher = platforms[i - 1]
            lower = platforms[i]
        difference_previous = higher - lower

        # Then finds the difference between the height of target
        # platform and the previous through one. It is necessary
        # to find which is higher and which is lower.
        if platforms[i] is max(platforms[i], platforms[i - 2]):
            higher = platforms[i]
            lower = platforms[i - 2]
        else: # platforms[i - 2] is max(platforms[i], platforms[i - 2]):
            higher = platforms[i - 2]
            lower = platforms[i]
        difference_through_one = 3 * (higher - lower)

        # Finds the amount of summary using different options to jump.
        option_1 = summary[i - 1] + difference_previous
        option_2 = summary[i - 2] + difference_through_one

        # Selects the lesser summary option and saves it
        # in summary list in a new position.
        if option_1 < option_2:
            summary.append(option_1)
        else: # option_1 >= option_2:
            summary.append(option_2)

    # Returns the minimum amount of energy to get to the last platform.
    return summary[-1]

# Input format:
# The first line shows the number of platforms (0 < n <= 30000).
# Next, the height of all platforms by one on an each line

# Catches the length of the platform's list.
length = int(input())

# Creates the list of the platforms.
platforms = []

# Catches heights of the all platforms.
for i in range(length):
    platforms.append(int(input()))

# Uses the function to find minimum amount of energy
# to get to the last platform.
answer = energy_game(platforms, length)

# Print the answer.
print(answer)