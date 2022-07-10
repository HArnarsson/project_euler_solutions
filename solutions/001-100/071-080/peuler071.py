# Project Euler - 71
# Date: 21/06/2022

# Made an educated guess that denominator is very close to 1 million

from math import gcd, inf
from time import time
start = time()

target = 3/7
min_dist = inf
lst = []
for i in range(1_000_000, 999_980, -1):
    j = 1
    while j/i<target:
        if target-j/i < min_dist and target-j/i>0:
            min_dist = target -j/i
            lst.append((j,i))
        j+=1
print(lst[-1])

print(time()-start)