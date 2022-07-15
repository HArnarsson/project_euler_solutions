# Project Euler - 24
# Date: 01/06/2022

from itertools import permutations

perm = permutations(list(range(0,10)))
counter = 0
for i in list(perm):
    if counter == 999999:
        print(i)
        break
    else:
        counter+=1