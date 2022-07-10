# Project Euler - 21
# Date 06/01/2022

from math import ceil, sqrt

def find_divisors(num):
    divisors = []
    n = 2
    while n<= ceil(sqrt(num)):
        if num%n == 0:
            divisors.append(n)
            divisors.append(num//n)
        n += 1
    divisors.append(1)
    return divisors

def d(num):
    return sum(find_divisors(num))

if __name__ == '__main__':
    num = 1
    summa = 0
    while num <10000:
        var = d(num)
        if num == d(var) and var != num:
            summa += num
        num += 1
    print(summa)
