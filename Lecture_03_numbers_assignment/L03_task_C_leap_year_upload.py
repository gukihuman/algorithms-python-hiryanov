def leap_year(year):
	"""
	Finds if the year is leap or not.

	:param year: the number of the year
	:return: 'YES' if the year is leap and 'NO' if it's not
	"""

	# Returns YES if the number of the year is divided by 4 without remainder
	# but at the same time is not divided by 100 without remainder.
	if year % 4 == 0 and year % 100 != 0:
		return 'YES'

	# Returns YES if the number of the year is divided by 400
	# without remainder.
	if year % 400 == 0:
		return 'YES'

	# Returns NO if every term is not true.
	return 'NO'


# Input format:
# A number of the year.

# Output format:
# 'YES' or 'NO' for the bissextile of the year.

# Catches the number of the year from input.
year = int(input())

# Uses the function to find if the year is leap or not.
answer = leap_year(year)

# Print the answer.
print(answer)