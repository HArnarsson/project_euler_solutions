# Project Euler - 110
# Date: 21/07/2022

# See resource for this problem for explanation
from math import prod

TARGET = 4*10**6
from math import ceil
min_dist = TARGET
limit = 25
nums = [3,5,7]
for a in range(1,limit):
    for b in range(0,limit):
        for c in range(0,limit):
            calc = ceil(1/2*(3**a)*(5**b)*(7**c))
            if 0 < calc-TARGET < min_dist:
                best_exponents = [a,b,c]
                best_num = calc
                min_dist = calc-TARGET

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]

best_factors = []
c=0
for i in range(len(best_exponents)-1,-1,-1):
    for _ in range(best_exponents[i]):
        for _ in range(i+1):
            best_factors.append(primes[c])
        c+=1

print(prod(best_factors))
