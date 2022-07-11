# Project Euler - 87
# Date: 11/07/2022

limit = 50_000_000

def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]

    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    for p in range(2, num+1):
        if prime[p]:
            yield p

primes=list(SieveOfEratosthenes(int(((limit-24)**(1/2))+1)))
lst = []
for a in primes:
    if a**4>limit:
        break
    for b in primes:
        if a**4+b**3>limit:
            break
        for c in primes:
            if a**4+b**3+c**2<limit:
                lst.append(a**4+b**3+c**2)

print(len(set(lst)))
