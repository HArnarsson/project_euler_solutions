# Project Euler - 108
# Date: 21/07/2022

from math import ceil, comb,sqrt
from collections import Counter
from time import time
 
def sieve(limit):
    spf = [0 for i in range(limit+1)]
    spf[1] = 1
    for i in range(2, limit):
        spf[i] = i
    for i in range(4, limit, 2):
        spf[i] = 2
 
    for i in range(3, ceil(sqrt(limit))):
        if (spf[i] == i):
            for j in range(i * i, limit, i):
                if (spf[j] == j):
                    spf[j] = i
    return spf
start = time()
spf = sieve(10**7)
print(time()-start)
def get_factorization(x,spf):
    ret = list()
    while (x != 1):
        ret.append(spf[x])
        x = x // spf[x]
    return ret

def psi(n,spf):
    factors = get_factorization(n,spf)
    a_s = Counter(factors)
    prod = 1/2
    for factor in a_s:
        prod*=(2*a_s[factor]+1)
    return ceil(prod)

n = 2
print(psi(n,spf))
while(True):
    if psi(n,spf)>1000:
        print(n)
        break
    n+=1
