# Project Euler - 104
# Date: 19/07/2022

from collections import Counter
from time import time

start = time()
def is_pandigital(num):
    return Counter(str(num)) == Counter(str(123456789))

def get_first_nine_digits_of_fib(n):
    # Note that f_n ≈ phi^n/sqrt(5) so log10(f_n) ≈ n*log10(phi)-log10(sqrt(5))
    # Precalculated vals to avoid error
    log10_phi = 0.20898764024997873
    log10sqrt5 = 0.3494850021680094
    log10f_n = n*log10_phi-log10sqrt5
    # fractional part gives info in digits, add 8 to shift it accross when raising to tenth power
    tenth_root_first_ten_dig = log10f_n - int(log10f_n)+8
    return int(10**tenth_root_first_ten_dig)


f_n1 = 1
f_n2 = 1
n=3
while(True):
    fib = (f_n1+f_n2) % 10**9
    if is_pandigital(fib):
        if is_pandigital(get_first_nine_digits_of_fib(n)):
            print(n)
            break
    f_n2 = f_n1
    f_n1 = fib
    n+=1

print(time()-start)
