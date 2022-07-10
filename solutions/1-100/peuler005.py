#Project Euler - 5
#Date: 04/05/2022
from math import ceil, sqrt

def is_prime(factor:int) -> bool:
    if factor == 2:
        return True
    n = 2
    while n<=ceil(sqrt(factor)):
        if factor % n == 0:
            return False
        n+=1
    return True
    
def find_factors(number:int) -> list:
    factor_list = []
    while number > 1:
        n=2
        while n<=ceil(sqrt(number)):
            if is_prime(number):
                factor_list.append(number)
                return factor_list
            elif number % n == 0:
                factor_list.append(n)
                number = number//n
                n+=1
                break
            n+=1
    return factor_list
if __name__ == '__main__':
    lst = []
    for i in range(2,11):
        lst.append(find_factors(i))
    print(lst)