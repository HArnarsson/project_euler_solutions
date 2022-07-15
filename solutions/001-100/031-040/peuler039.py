# Project Euler - 39
# Date: 03/06/2022

from math import ceil
def make_squares(limit):
    x = 1
    lst = []
    while x**2<limit:
        lst.append(x**2)
        x+=1
    return lst
squares = make_squares((10**3)**2)
# perimeter must be even
# b = (p**2-2pa)/(2p-2a) from a+b+c=p and a**2+b**2=c**2
# a+b+c = p and a<=b<c without loss of generality
max_num = 0
for p in range(2,1001, 2):
    temp = 0
    for a in range(ceil(p/3)):
        b = (p**2-2*p*a)%(2*p-2*a) # only need to see if it divides
        if b == 0:
            temp += 1
    if temp>max_num:
        max_num = temp
        answer = p
print(answer)