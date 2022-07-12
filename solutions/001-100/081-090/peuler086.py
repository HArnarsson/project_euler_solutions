# Project Euler - 86
# Date: 12/07/2022

from math import sqrt
from time import time

is_square = lambda n : int(sqrt(n))**2 == n

is_shortest_path_int = lambda a,b_c : is_square(a**2+(b_c)**2)

num_solns = [0,0]
a=2
start = time()
while(True):
    count = 0
    for b_c in range(2,2*a+1):
        # Tvö tilfelli:
        # 1: b+c<=a, þá má velja b+c á int((b+c)/2) vegu, sbr. 1+5,2+4,3+3 = 6
        # 2: 2a>=b+c>a, þetta er flóknara, b getur tekið gildi frá (b_c+1)//2 upp í 2*a-1 í heildina, en viljum bara að b taki gildi frá (b_c+1)//2 upp í a
        #    en það eru a-(b_c+1)//2+1 
        if is_shortest_path_int(a,b_c):
            if b_c<=a:
                count += b_c//2
            else:
                count += a-(b_c-1)//2
    num_solns.append(count+num_solns[a-1])
    if num_solns[a]>1000000:
        break
    a+=1

print(num_solns.index(num_solns[-1]))
print(time()-start)
