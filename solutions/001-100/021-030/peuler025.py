# Project Euler - 25
# Date: 01/06/2022

def find_1000_digit_fib():
    fibs = []
    fibs.append(1)
    fibs.append(1)
    fib = 1
    while len(str(fib))<1000:
        fibs.append(fib)
        fib = fibs[fibs.index(fib)]+fibs[fibs.index(fib)-1]
    print(len(fibs))

find_1000_digit_fib()