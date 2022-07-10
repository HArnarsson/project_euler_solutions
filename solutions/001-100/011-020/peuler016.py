# Project Euler - 16
# Date: 31/05/2022

def digit_sum(num):
    sum = 0
    for digit in str(num):
        sum += int(digit)
    return sum

def find_sum(max):
    n = 1
    lst = []
    while n<=max:
        lst.append(digit_sum(2**n))
        n+=1
    return lst

print((find_sum(1000)))