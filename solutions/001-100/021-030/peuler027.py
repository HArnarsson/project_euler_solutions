# Project Euler - 27
# Date: 01/06/2022

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
def is_prime(n):
    for i in range(2,int(abs(n)**0.5)+1):
        if n%i == 0:
            return False
    return True
temp = list(SieveOfEratosthenes(1000))
temp_2 = [-prime for prime in temp]
listy = temp_2 + temp
b_vals = list(SieveOfEratosthenes(1000))
a_vals = list(range(-999,1000,2))
primes = list(SieveOfEratosthenes(10**7))
def calculate_quadratic(n,a,b):
    return int(abs(n**2 + a*n + b))
def find_num_consecutive_primes(primes, a: int, b:int):
    n=0
    while(True):
        if is_prime(calculate_quadratic(n,a,b)):
            n+=1
        else:
            break
    return n
max_ab = 0
for i in (a_vals):
    for j in (b_vals):
        var = find_num_consecutive_primes(primes,i,j)
        if var>max_ab:
            max_ab = var
            final_a = i
            final_b = j
        

print(final_a*final_b)