# Project Euler - 74
# Date: 12/07/2022

from math import factorial as fact
from time import time as t

def calc_digit_fact(num):
    summa = 0
    for dig in str(num):
        summa += fact(int(dig))
    return summa

def calc_length_chain(num, lengths):
    sett = set()
    l = 0
    while(True):
        if num < len(lengths):
            if lengths[num] != 0:
                return l+lengths[num]
        if num in sett:
            return l
        else:
            sett.add(num)
            num = calc_digit_fact(num)
            l+=1

if __name__ == "__main__":
    start = t()
    c = 0
    lengths = [0]*1_000_001
    for i in range(1,1000_001):
        temp = calc_length_chain(i, lengths)
        lengths[i] = temp
        if temp == 60:
            c+=1
    print(c)
    print(t()-start)
    
