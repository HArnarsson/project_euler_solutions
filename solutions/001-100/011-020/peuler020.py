# Project Euler - 20
# Date: 31/05/2022

from math import factorial
def digit_sum(num):
    sum = 0
    num = str(num)
    for digit in range(len((num))):
        sum += int(num[digit])
    return sum

print(digit_sum(factorial(100)))