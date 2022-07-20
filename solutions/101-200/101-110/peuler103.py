# Project Euler - 103
# Date: 20/07/2022

from itertools import combinations, chain
from time import time
og = [20,31,38,39,40,42,45]

def powerset(iterable):
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

# Brute Force method

candidates = []
for r in range(1,5):
    for comb in list(combinations(range(7), r)):
        for j in range(1,4):
            candidates.append([og[k] if k not in comb else og[k]-j for k in range(len(og))])

print(candidates)
for cand in candidates:
    if condition1(cand) and condition2(cand):
        print(cand)
        
# Here nothing was printed, so I tested the "og" solution and it turns out the "near-optimum" algorithm was optimal in this case. ans: 20313839404245
