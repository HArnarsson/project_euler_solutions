# Project Euler - 60
# Date: 11/07/2022

from time import time
start = time()
def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]

    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    for p in range(2, num+1):
        if prime[p] and (p%3==1 or p==3):
            yield p

primes = list(SieveOfEratosthenes(10000))

def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(abs(n)**0.5)+1):
        if n%i == 0:
            return False
    return True

def is_nice_pair(num1,num2):
    return is_prime(int(str(num1)+str(num2))) and is_prime(int(str(num2)+str(num1)))

def gen_pairs(p):
    lst = []
    for p2 in primes:
        if is_nice_pair(p,p2):
            lst.append(p2)
    return lst

pairs = dict()
result = 100_000

for a in range(len(primes)):
    if primes[a]*5 >= result:
        break
    if not pairs.get(primes[a], False):
        pairs[primes[a]] = gen_pairs(primes[a])

    for b in range(a,len(primes)):
        if primes[a] + primes[b]*4>= result:
            break
        if primes[b] not in pairs[primes[a]]:
            continue
        if not pairs.get(primes[b], False):
            pairs[primes[b]] = gen_pairs(primes[b])
        
        for c in range(b, len(primes)):
            if primes[a] + primes[b] + primes[c]*3 >= result:
                break
            if (primes[c] not in pairs[primes[a]]) or (primes[c] not in pairs[primes[b]]):
                continue
            if not pairs.get(primes[c], False):
                pairs[primes[c]] = gen_pairs(primes[c])

            for d in range(c, len(primes)):
                if primes[a]+primes[b]+primes[c]+primes[d]*2>=result:
                    break
                if (primes[d] not in pairs[primes[c]]) or (primes[d] not in pairs[primes[b]]) or (primes[d] not in pairs[primes[a]]):
                    continue
                if not pairs.get(primes[d], False):
                    pairs[primes[d]] = gen_pairs(primes[d])

                for e in range(d, len(primes)):
                    if (primes[e] not in pairs[primes[d]]) or (primes[e] not in pairs[primes[c]]) or (primes[e] not in pairs[primes[b]]) or (primes[e] not in pairs[primes[a]]):
                        continue

                    temp_result = primes[a] + primes[b] + primes[c] + primes[d] + primes[e]
                    if result>temp_result:
                        result = temp_result
print(result)
print(time()-start)
