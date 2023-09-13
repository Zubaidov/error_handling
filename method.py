""" from modules import calc
from modules.calc import log as lg
import math
import sys

n = calc.sum(5, 5)
x = lg(3,4)
print(n)
print(x)
print(type(calc))
print(type(math))

print(sys.path) """

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)