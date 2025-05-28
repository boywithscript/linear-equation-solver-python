# linear-equation-solver-python
from fractions import Fraction

a = float(input("a = "))
b = int(input("b = "))

def solve(a, b):
    dec = Fraction(a).limit_denominator()
    exponent = b ** 2
    result = exponent / dec
    return int(result)

print (solve(a, b))
"""
Example
if a = 0.2 and b = 5²
then result is 125

"""

    