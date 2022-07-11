# Project Euler - 61
# Date: 11/07/2022

from time import time

start = time()
gen_tri = lambda n : n*(n+1)//2
gen_sq = lambda n: n**2
gen_pent = lambda n: n*(3*n-1)//2
gen_hex = lambda n: n*(2*n-1)
gen_hept = lambda n: n*(5*n-3)//2
gen_oct = lambda n: n*(3*n-2)

tri, sq, pent, hex, hept, oct = [],[],[],[],[],[]

n=1
while(gen_tri(n)<10_000):
    tri.append(gen_tri(n))
    n+=1
tri = [tri[i] for i in range(len(tri)) if tri[i]>=1000]

n=1
while(gen_sq(n)<10_000):
    sq.append(gen_sq(n))
    n+=1
sq = [sq[i] for i in range(len(sq)) if sq[i]>=1000]

n=1
while(gen_pent(n)<10_000):
    pent.append(gen_pent(n))
    n+=1
pent = [pent[i] for i in range(len(pent)) if pent[i]>=1000]

n=1
while(gen_hex(n)<10_000):
    hex.append(gen_hex(n))
    n+=1
hex = [hex[i] for i in range(len(hex)) if hex[i]>=1000]

n=1
while(gen_hept(n)<10_000):
    hept.append(gen_hept(n))
    n+=1
hept = [hept[i] for i in range(len(hept)) if hept[i]>=1000]

n=1
while(gen_oct(n)<10_000):
    oct.append(gen_oct(n))
    n+=1
oct = [oct[i] for i in range(len(oct)) if oct[i]>=1000]
poly_list = [tri, sq, pent, hex, hept]

def is_cyclic(num1,num2):
    return num1%100 == num2//100

def find_solution(oct, poly_list):
    for oct_num in oct:
        for poly1 in poly_list:
            for num1 in poly1:
                if is_cyclic(oct_num,num1):
                    poly_list1 = poly_list[:]
                    poly_list1.remove(poly1)
                    for poly2 in poly_list1:
                        for num2 in poly2:
                            if is_cyclic(num1,num2):
                                poly_list2 = poly_list1[:]
                                poly_list2.remove(poly2)
                                for poly3 in poly_list2:
                                    for num3 in poly3:
                                        if is_cyclic(num2,num3):
                                            poly_list3 = poly_list2[:]
                                            poly_list3.remove(poly3)
                                            for poly4 in poly_list3:
                                                for num4 in poly4:
                                                    if is_cyclic(num3,num4):
                                                        poly_list4 = poly_list3[:]
                                                        poly_list4.remove(poly4)
                                                        for poly5 in poly_list4:
                                                            for num5 in poly5:
                                                                if is_cyclic(num4,num5):
                                                                    if is_cyclic(num5,oct_num):
                                                                        print(oct_num+num1+num2+num3+num4+num5)
                                                                        return None
find_solution(oct, poly_list)
