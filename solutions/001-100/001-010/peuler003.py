#Project Euler - 3
#Date: 04/05/2022
from math import ceil,sqrt
def is_prime(factor:int) -> bool:
    if factor == 2:
        return True
    n = 2
    while n<=ceil(sqrt(factor)):
        if factor % n == 0:
            return False
        n+=1
    return True

    
def find_prime_factors(number:int) -> list:
    if is_prime(number):
        return [number]
    prime_factors = []
    n=2
    while n<=ceil(sqrt(number)):
        if number % n == 0 and is_prime(n):
            prime_factors.append(n)
        n+=1
    return prime_factors
if __name__ == '__main__':
    print(is_prime(9))

