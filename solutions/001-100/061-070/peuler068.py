# Project Euler - 68
# Date: 13/07/2022

from itertools import permutations
from time import time
start = time()

# Ef það er til lausn þ.a. 6,7,8,9,10 séu ytri nóður, þá er stærsta lausnin af því tagi stærsta lausnin
def is_solution(soln):
    summa = sum(soln[0])
    for i in range(1,len(soln)):
        if sum(soln[i])!=summa:
            return False
    return True

def solution_to_int(solution):
    to_return = ""
    for b in solution:
        for num in b:
            to_return += str(num)
    return int(to_return)

outer_nodes = [7,8,9,10]
inner_nodes = [1,2,3,4,5]

perms_outer = list(permutations(outer_nodes))
perms_inner = list(permutations(inner_nodes))

solutions = []
for outer in perms_outer:
    outer = [6] + list(outer)
    for inner in perms_inner:
        solution = []
        for i in range(len(inner)):
            solution.append([outer[i],inner[i],inner[(i+1)%5]])
        if is_solution(solution):
            solutions.append(solution_to_int(solution))

print(max(solutions))
print(time()-start)
