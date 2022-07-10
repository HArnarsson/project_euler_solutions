#Project Euler - 7
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

lst = []
i = 2
while(len(lst)<=10001):
    if is_prime(i):
        lst.append(i)
    i+=1
print(lst[10000])