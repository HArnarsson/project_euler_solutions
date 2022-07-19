# Project Euler - 101
# Date: 19/07/2022

import numpy.linalg as la
import numpy as np
from time import time
start = time()

# See resource for this problem for explanation of math
def get_O(m,u_n):
    A = np.arange(m**2)
    A = A.reshape(m,m)
    for i in range(1,m+1):
        for j in range(m):
            A[i-1][j] = i**(j)
    B = np.array([u_n(k) for k in range(1,m+1)])
    a = la.solve(A,B)
    def O(n):
        summa = 0
        for i in range(len(a)):
            summa += round(a[i])*n**i
        return summa
    return O

u_n = lambda n: 1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10
summa = 0
for m in range(1,11):
    O_m = get_O(m,u_n)
    summa += O_m(m+1)
print(summa)
print(time() - start)
