# Project Euler - 34
# Date: 02/06/2022

from math import factorial
tally = 0
for i in range(3,1000000):
    summa = 0
    temp = str(i)
    for digit in temp:
        summa += factorial(int(digit))
    if summa == i:
        tally += i
print(tally)