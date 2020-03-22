"""
Finds a hypotenuse from two other sides (legs) of a triangle
using Pythagorean theorem.
"""

# Sets lengths of the legs of the triangle.
a, b = 179, 197

# Calculate the hypotenuse.
c = (a ** 2 + b ** 2) ** 0.5

# You should see 266.1766330841233
print(c)