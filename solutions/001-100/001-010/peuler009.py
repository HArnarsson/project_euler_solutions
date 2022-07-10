#Project Euler - 9
#Date: 04/05/2022

from math import sqrt
for a in range(1,1000):
    for b in range(1,1000):
        c_squared = a**2 + b**2
        c = sqrt(c_squared)
        if c % 1 <10**-3 or c%1 >0.999:
            if a + b + c == 1000:
                print((a*b*c))
            break
        else:
            continue