# Project Euler - 187
# Date: 18/07/2022

from math import sqrt
def is_prime(n):
	result = [True] * (n + 1)
	result[0] = result[1] = False
	for i in range(int(sqrt(n)) + 1):
		if result[i]:
			for j in range(2 * i, len(result), i):
				result[j] = False
	return result

def get_primes(limit):
    bool_primes = is_prime(limit)
    return [i for i in range(len(bool_primes)) if bool_primes[i]]
    
def pi(limit,primes):
    '''prime counting function as an array'''
    pi = [0]*(limit+1)
    num_primes = 0
    for i in range(1, limit + 1):
        while True:
            if primes[num_primes] > i:
                pi[i] = num_primes
                break
            num_primes += 1
    return pi

limit = 100_000_000
primes = get_primes(limit//2+100)
num_primes = pi(limit//2,primes)
sum_limit = num_primes[int(sqrt(limit))]
total = 0

for k in range(1, sum_limit + 1):
    total += num_primes[int(limit/primes[k-1])] - k + 1
print(total)
