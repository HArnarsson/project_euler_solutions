#Project Euler - 12
#Date: 13/5/2022 

from itertools import count
def sieve_of_erastosthenes(n:int, include_squared=False) -> list:
    prime = [True for i in range(n+1)]
    p=2
    while(p<=n):
        i=0
        k=0
        while k<=n:
            prime[k]=False
            k = p*(2+i)
            i+=1
        p+=1
    prime[1] = False
    if include_squared:
        prime_squared = [False for i in range(n*n+1)]
        for i in range(len(prime)):
            if prime[i]:
                prime_squared[i*i] = True
        return (prime,prime_squared)
    return prime


is_prime = sieve_of_erastosthenes(50000, include_squared=True)[0]
is_prime_squared = sieve_of_erastosthenes(50000,include_squared=True)[1]
def count_divisors(n:int) -> int:
    if n==1:
        return 1
    cnt = 1
    primes = [k for k in range(len(is_prime)) if is_prime[k]]
    i = 0
    while(primes[i]**3<n):
        temp = 1
        while(n%primes[i]==0):
            n = n/primes[i]
            temp +=1
        cnt *= temp
        i+=1
    n = int(n)
    if is_prime[n]:
        cnt*=2
    elif is_prime_squared[n]:
        cnt*=3
    elif n!=1:
        cnt*=4
    return cnt
def triangle_num(index:int) -> int:
    return index*(index+1)//2
if __name__ == '__main__':
    n = 10000
    print(triangle_num(10000))
    while(True):
        triangle_num_n = triangle_num(n)
        print(f'n is {n} percentage is {triangle_num_n/76576500*100:.2f} %')
        k = n//2
        if n % 2 == 0:
            (a,b) = (k,2*k+1)
        elif n % 2 != 0:
            (a,b) = (k+1,2*k+1)
        number_of_divisors = count_divisors(a)*count_divisors(b)
        if number_of_divisors>500:
            print(triangle_num_n)
            break
        n+=1
    