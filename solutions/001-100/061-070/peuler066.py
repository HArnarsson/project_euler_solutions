# Project Euler - 66
# Date: 12/07/2022

from math import sqrt,gcd

is_square = lambda n : int(sqrt(n))**2 == n
def find_cont_inf_frac(n):
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
    return [a,b]

def solve_diophantine(D):
    if is_square(D):
        return 0,0
    start_val = [find_cont_inf_frac(D)[0]]
    pattern = find_cont_inf_frac(D)[1:]
    seq = start_val+pattern
    i = 1
    while(True):
        if i>=len(seq):
            seq+=pattern
        h,k = find_convergent(seq,i)
        if h**2-D*k**2 == 1:
            return h,k
        i+=1

if __name__ == '__main__':
    max = 0
    for d in range(1,1001):
        x,y = solve_diophantine(d)
        if x > max:
            max = x
            val = d
    print(val)
