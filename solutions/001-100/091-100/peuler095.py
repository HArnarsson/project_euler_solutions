# Project Euler - 95
# Date: 15/07/2022

from time import time as t

def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]

    p = 2
    while (p * p <= num):
 
        if (prime[p] == True):
 
            # Updating all multiples of p
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
 
    for p in range(2, num+1):
        if prime[p]:
            yield p
        
primes = list(SieveOfEratosthenes(10**6))

def calc_sum_div(n,primes):
    og = n
    summ = 1
    i = 0
    while(True):
        p = primes[i]
        if p**2>n: 
            break
        temp_sum = summ
        while(n%p) == 0:
            n//=p
            summ = summ*p + temp_sum
        i+=1
    if n>1:
        summ*=(n+1)
    return summ - og

def calc_length_chain(num, lengths, primes):
    sett = set()
    l = 0
    og = num
    while(True):
        num = calc_sum_div(num,primes)
        if num>len(lengths):
            return -1
        if lengths[num] == -1:
            return -1
        if lengths[num] != 0:
            return lengths[num]
        if num in sett:
            return -1
        if num == og:
            return l
        sett.add(num)
        l+=1

start = t()
lengths = [0]*1_000_001

for i in range(2,1_000_001):
    if i%1000 == 0:
        print(i)
    temp = calc_length_chain(i,lengths,primes)
    lengths[i] = temp
print(lengths.index(max(lengths)))
print(t()-start)
