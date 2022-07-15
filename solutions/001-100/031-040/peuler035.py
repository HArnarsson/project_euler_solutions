# Project Euler - 35
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
    for i in range(2,int(abs(n)**0.5)+1):
        if n%i == 0:
            return False
    return True

def make_list_permutations(prime):
    prime = str(prime)
    lst = []
    if len(prime) == 1:
        return [int(prime)]
    for i in range(len(prime)-1):
        prime = prime[1:]+prime[0]
        lst.append(int(prime))
    return lst
circular_primes = []
for prime in all_primes:
    var = True
    perms = make_list_permutations(prime)
    for num in perms:
        if is_prime(num):
            continue
        else:
            var = False
            break
    if var:
        circular_primes.append(prime)


print(len(circular_primes))