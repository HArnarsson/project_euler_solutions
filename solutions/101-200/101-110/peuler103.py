from itertools import combinations
from time import time
og = [20,31,38,39,40,42,45]

def print_max_and_min_sets(cand):
    if len(cand)%2 == 0:
        max_min = len(cand)//2
        for i in range(max_min,1,-1):
            if(sum(cand[:i]) > sum(cand[-(i-1):])):
                continue
            else:
                return False
        return True
    elif len(cand)%2 != 0:
        max_min = len(cand)//2+1
        for i in range(max_min,1,-1):
            if(sum(cand[:i]) > sum(cand[-(i-1):])):
                continue
            else:
                return False

print_max_and_min_sets(og)
def has_same_sum(cand:list):
    for length in range(2,7):
        for comb in list(combinations(cand,length)):
            temp = [cand[i] for i in range(len(cand)) if cand[i] not in comb]
            for r in range(1,len(temp)+1):
                for subcomb in list(combinations(temp,r)):
                    if sum(subcomb) == sum(comb):
                        return True
    return False

# Brute Force method

candidates = []
for r in range(1,5):
    for comb in list(combinations(range(7), r)):
        for j in range(1,4):
            candidates.append([og[k] if k not in comb else og[k]-j for k in range(len(og))])

print(candidates)
for cand in candidates:
    if has_same_sum(cand) and print_max_and_min_sets(cand):
        print(cand)
        
# Here nothing was printed, so I tested the "og" solution and it turns out the "near-optimum" algorithm was optimal in this case. ans: 20313839404245
