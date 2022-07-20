# Project Euler - 105
# Date: 20/07/2022

from itertools import combinations, chain
from time import time

def powerset(iterable):
    # From itertools website
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1,len(s)+1))

def condition2(cand):
    sum1 = cand[0]
    sum2 = 0
    for i in range(len(cand)//2):
        sum1+=cand[i+1]
        sum2+=cand[len(cand)-i-1]
        if sum1<=sum2:
            return False
    return True

def condition1(cand):
    all_subsets = powerset(cand)
    for sub in all_subsets:
        summ = sum(sub)
        for sub2 in powerset(set(cand)-set(sub)):
            if sum(sub2) == summ:
                print(sub,sub2)
                return False
    return True

candidates = []
with open("lib\\101-200\\peuler_resource105.txt") as file:
    for row in file:
        candidates.append(row[:-1].split(','))

for i in range(len(candidates)):
    for j in range(len(candidates[i])):
        candidates[i][j] = int(candidates[i][j])
    candidates[i].sort()
print(len(candidates))
summa = 0
for cand in candidates:
    if condition2(cand):
        if condition1(cand):
            summa += sum(cand)
print(summa)
