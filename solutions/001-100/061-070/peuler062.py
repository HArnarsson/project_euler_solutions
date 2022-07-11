# Project Euler - 62
# Date: 11/07/2022

from itertools import permutations
import collections

def gen_cubes(limit):
    a=1
    sett = []
    while a<limit:
        sett.append(a**3)
        a+=1
    return sett

def get_largest_permutation(num):
    k = num
    digits = [0]*10
    return_val = 0
    while(k>0):
        digits[k%10]+=1
        k//=10
    for i in range(9,-1,-1):
        for _ in range(digits[i]):
            return_val = return_val*10 +i
    return return_val

def is_permutation(a, b):
    a,b = str(a),str(b)
    d = collections.defaultdict(int)
    for x in a:
        if x == '0':
            continue
        d[x] += 1
    for x in b:
        if x == '0':
            continue
        d[x] -= 1
    return not any(d.values())

counter = collections.defaultdict(int)

i=1
while(True):
    counter[get_largest_permutation(i**3)]+=1
    if counter[get_largest_permutation(i**3)] == 5:
        largest_cube = i**3
        break
    i+=1

cubes = gen_cubes(i)
for cube in cubes:
    if is_permutation(cube,largest_cube):
        print(cube)
        break
