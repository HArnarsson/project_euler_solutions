from math import inf, prod

TARGET = 4*10**6
from math import ceil
min_dist = TARGET
limit = 15
best_number = float(inf)
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

def calc_num(best_exponents,primes):
    best_factors = []
    c=0
    for i in range(len(best_exponents)-1,-1,-1):
        for _ in range(best_exponents[i]):
            for _ in range(i+1):
                best_factors.append(primes[c])
            c+=1
    return prod(best_factors)

primes = list(SieveOfEratosthenes(1000))
for a in range(1,limit):
    for b in range(0,limit):
        for c in range(0,limit//2):
            for d in range(0,limit//2):
                calc = ceil(1/2*(3**a)*(5**b)*(7**c)*(9**d))
                if calc>TARGET:
                    if calc_num([a,b,c,d],primes) < best_number:
                        best_exponents = [a,b,c,d]
                        best_num = calc
                        min_dist = calc-TARGET
                        best_number = calc_num(best_exponents,primes)

print(best_number)
