# Project Euler - 91 
# Date: 05/07/2022

# There is some not so trivial math going on behind the scenes here, I might TeX up a rough draft of it sometime

from math import gcd

SIZE = 50

counter = 0
for x in range(1,SIZE):
    for y in range(1,SIZE+1):
        temp = gcd(x,y)
        counter += min((SIZE-x)*temp//y, y*temp//x)
    
print(3*SIZE**2 + 2*counter)