# Project Euler - 29
# Date: 01/06/2022

listy = []
for a in range(2,101):
    for b in range(2,101):
        listy.append(a**b)
listy = list(set(listy))
print(len(listy))