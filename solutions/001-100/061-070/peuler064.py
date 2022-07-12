#Project Euler - 64
# Date: 06/07/2022

from math import sqrt, gcd

is_square = lambda n : int(sqrt(n))**2 == n
def find_len_cont_inf_frac(n):
    if is_square(n):
        return 0
    start_val = int(sqrt(n))
    m = start_val
    a = n-m**2
    c=1
    counter = 0
    while(True):
        if a == 1 and m == start_val:
            counter += 1
            break
        b = int((sqrt(n) + m)//a)
        counter += 1
        div = gcd(a,c*(n-(a*b-m)**2))
        m,c,a = a*b-m, a//div, c*(n-(a*b-m)**2)//div
    return counter

odd_periods = 0
for n in range(10_001):
    odd_periods += int(find_len_cont_inf_frac(n)%2 == 1)


print(odd_periods)
