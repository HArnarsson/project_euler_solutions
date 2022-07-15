# Project Euler - 32
# Date: 02/06/2022

from math import ceil, sqrt

def find_divisors(num):
    divisors = []
    n = 2
    while n<= ceil(sqrt(num)):
        if num%n == 0:
            divisors.append([n,num//n])
        n += 1
    return divisors

def is_pandigital(str1,str2,str3):
    if len(str(str1)) + len(str(str2))>6:
        return False
    stringy = str(str1) + str(str2) + str(str3)
    nums = ['1','2','3','4','5','6','7','8','9']
    for digit in stringy:
        if digit in nums:
            nums.remove(digit)
            continue
        else:
            return False
    if nums == []:
        return True
    else:
        return False

pandigital_nums = []
for num in range(1000,100001):
    divisors = find_divisors(num)
    for i in range(len(divisors)):
        if is_pandigital(divisors[i][0], divisors[i][1], num) and num not in pandigital_nums:
            pandigital_nums.append(num)
print(sum(pandigital_nums))