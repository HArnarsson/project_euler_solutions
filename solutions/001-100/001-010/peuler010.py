#Project Euler - 10
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
sum = 0
for i in range(2,2000001):
    if i%2==0:
        continue
    if i%3==0:
        continue
    elif is_prime(i):
        sum+=i
print(sum)