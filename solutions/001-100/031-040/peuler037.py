# Project Euler - 37
# Date: 02/06/2022

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
all_primes = list(SieveOfEratosthenes(10**6))
def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(abs(n)**0.5)+1):
        if n%i == 0:
            return False
    return True

primes = list(SieveOfEratosthenes(10**6))
primes.remove(2)
primes.remove(3)
primes.remove(5)
primes.remove(7)
truncatable_primes = []
def is_left_trunc(prime):
    prime = str(prime)
    for i in range(1,len(prime)):
        if is_prime(int(prime[i:])):
            continue
        else:
            return False
    return True
def is_right_trunc(prime):
    prime = str(prime)
    for i in range(1,len(prime)):
        if is_prime(int(prime[:-i])):
            continue
        else:
            return False
    return True

while(len(truncatable_primes) < 11):
    for prime in primes:
        if is_left_trunc(prime) and is_right_trunc(prime):
            truncatable_primes.append(prime)
print(sum(truncatable_primes))