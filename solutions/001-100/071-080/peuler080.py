# Project Euler - 80
# Date: 11/07/2022

from math import sqrt,gcd

def find_cont_inf_frac(n):
    is_square = lambda n : int(sqrt(n))**2 == n
    seq = []
    if is_square(n):
        return []
    start_val = int(sqrt(n))
    seq.append(start_val)
    m = start_val
    a = n-m**2
    c=1
    counter = 0
    while(True):
        if a == 1 and m == start_val:
            counter += 1
            seq.append(int(sqrt(n)+m))
            break
        b = int((sqrt(n) + m)//a)
        seq.append(b)
        counter += 1
        div = gcd(a,c*(n-(a*b-m)**2))
        m,c,a = a*b-m, a//div, c*(n-(a*b-m)**2)//div
    return seq

def find_convergent(seq, start):
    if start == 1:
        return [seq[0],1]
    a,b = 1,seq[start-1]
    for i in range(start-2,0,-1):
        a,b = b,a+b*seq[i]
    a,b = seq[0]*b+a, b
    return a,b

def find_decimal_sqrt(n):
    seq = find_cont_inf_frac(n) + find_cont_inf_frac(n)[1:]*1000
    return find_convergent(seq,1000)

def long_division(a,b):
    lst = []    
    while len(lst)<100:      
        lst.append(a // b)
        a = a % b * 10
    return lst

if __name__ == "__main__":
    total = 0
    is_square = lambda n : int(sqrt(n))**2 == n
    for i in range(1,101):
        if is_square(i):
            continue
        else:
            a,b = find_decimal_sqrt(i)
            total += sum(long_division(a,b))
    print(total)
