# Project Euler - 65
# Date: 05/07/2022

def digit_sum(num):
    summa = 0
    for char in str(num):
        summa += int(char)
    return summa
listy = [2,1]
for i in range(3,101):
    if i%3==0:
        listy.append(2*(i//3))
    else:
        listy.append(1)

START = 100-1
a,b = 1,listy[START-1]+1
for i in range(START-2,0,-1):
    a,b = b,a+b*listy[i]
print(digit_sum(2*b+a))
