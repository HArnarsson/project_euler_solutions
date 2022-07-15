# Project Euler - 28
# Date: 01/06/2022

summa = 1
top_right = 1
for l in range(1,501):
    for j in range(1,5):
        summa += j*(2*l)+top_right
    top_right = 4*2*l+top_right

print(summa)