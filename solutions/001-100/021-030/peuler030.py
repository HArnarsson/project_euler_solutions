# Project Euler - 30
# Date: 01/06/2022

def is_sum_of_fifth_pow(num):
    summ = 0
    for dig in str(num):
        summ += int(dig)**5
    return num == summ

total = 0
for i in range(2,1_000_001):
    if is_sum_of_fifth_pow(i):
        total += i
print(total)