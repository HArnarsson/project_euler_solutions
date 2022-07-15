# Project Euler - 23
# Date: 01/06/2022

from math import ceil, sqrt

def find_divisors(num):
    if num == 1:
        return [1]
    divisors = []
    n = 2
    while n<= ceil(sqrt(num)):
        if num%n == 0 and num != n:
            divisors.append(n)
            if num//n != n:
                divisors.append(num//n)
        n += 1
    divisors.append(1)
    divisors = list(set(divisors))
    return divisors

def is_abundant_number(num):
    if sum(find_divisors(num))>num:
        return True
    else:
        return False

abundant_numbers = []
for i in range(1,28124):
    if is_abundant_number(i):
        abundant_numbers.append(i)

possible_sums = []
for i in range(len(abundant_numbers)):
    for j in range(len(abundant_numbers)):
        possible_sums.append(abundant_numbers[i] + abundant_numbers[j])
possible_sums = list(set(possible_sums))

numbers = list(range(1,28124))

for i in range(len(possible_sums)):
    try:
        numbers.remove(possible_sums[i])
    except:
        pass

print(sum(numbers))