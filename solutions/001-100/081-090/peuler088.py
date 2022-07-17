from collections import Counter
from itertools import permutations
from math import ceil,inf, log2,sqrt,prod
from time import time

def get_factorization(x, spf):
    ret = list()
    while (x != 1):
        ret.append(spf[x])
        x = x // spf[x]
    return ret

all_factorizations = []

max_num_factors = int(log2(24000))

for num_factors in range(2,15):
    print(num_factors)
    for a in range(2,ceil((12_000**(1/num_factors)))+1):
        for b in range(2,24000//a):
            if num_factors == 2:
                all_factorizations.append([a,b])
            if num_factors > 2:
                for c in range(2,24000//(a*b)+1):
                    if num_factors == 3:
                        all_factorizations.append([a,b,c])
                    if num_factors > 3:
                        for d in range(2,24000//(a*b*c)+1):
                            if num_factors == 4:
                                all_factorizations.append([a,b,c,d])
                            if num_factors>4:
                                for e in range(2,24000//(a*b*c*d)+1):
                                    if num_factors == 5:
                                        all_factorizations.append([a,b,c,d,e])
                                    if num_factors>5:
                                        for f in range(2,24000//(a*b*c*d*e)+1):
                                            if num_factors == 6:
                                                all_factorizations.append([a,b,c,d,e,f])
                                            if num_factors > 6:
                                                for g in range(2,24000//(a*b*c*d*e*f)+1):
                                                    if num_factors == 7:
                                                        all_factorizations.append([a,b,c,d,e,f,g])
                                                    if num_factors>6:
                                                        for h in range(2,24000//(a*b*c*d*e*f*g)+1):
                                                            if num_factors == 8:
                                                                all_factorizations.append([a,b,c,d,e,f,g,h])
                                                            if num_factors>8:
                                                                for i in range(2,24000//(a*b*c*d*e*f*g*h)+1):
                                                                    if num_factors == 9:
                                                                        all_factorizations.append([a,b,c,d,e,f,g,h,i])
                                                                    if num_factors>9:
                                                                        for j in range(2,24000//(a*b*c*d*e*f*g*h*i)+1):
                                                                            if num_factors==10:
                                                                                all_factorizations.append([a,b,c,d,e,f,g,h,i,j])
                                                                            if num_factors>10:
                                                                                for k in range(2,24000//(a*b*c*d*e*f*g*h*i*j)+1):
                                                                                    if num_factors==11:
                                                                                        all_factorizations.append([a,b,c,d,e,f,g,h,i,j,k])
                                                                                    if num_factors>11:
                                                                                        for l in range(2,24000//(a*b*c*d*e*f*g*h*i*j*k)+1):
                                                                                            if num_factors == 12:
                                                                                                all_factorizations.append([a,b,c,d,e,f,g,h,i,j,k,l])
                                                                                            if num_factors>12:
                                                                                                for m in range(2,24000//(a*b*c*d*e*f*g*h*i*j*k*l)+1):
                                                                                                    if num_factors == 13:
                                                                                                        all_factorizations.append([a,b,c,d,e,f,g,h,i,j,k,l,m])
                                                                                                    if num_factors>13:
                                                                                                        for n in range(2,24000//(a*b*c*d*e*f*g*h*i*j*k*l*m)+1):
                                                                                                            if num_factors == 14:
                                                                                                                all_factorizations.append([a,b,c,d,e,f,g,h,i,j,k,l,m,n])

def find_k_from_fact(factorization):
    num = prod(factorization)
    summ = sum(factorization)
    if num == summ:
        return len(factorization)
    c = num - summ
    return len(factorization)+c

k = [float(inf)]*(2_000_000+1)
for factorization in all_factorizations:
    k_i = find_k_from_fact(factorization)
    if prod(factorization)<k[k_i]:
        k[k_i] = prod(factorization)

print(sum(set(k[2:12_001])))