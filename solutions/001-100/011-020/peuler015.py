# Project Euler -15
# Date: 31/05/2022

from math import factorial
n = 40
r = 20
def combinations(n,r):
    return factorial(n)//(factorial(n-r)*factorial(r))
print(combinations(n,r))