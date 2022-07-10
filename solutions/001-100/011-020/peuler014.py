# Project Euler - 14
# Date: 17/05/2022

lengths = [0]*1_000_001
def get_collatz_length(num, lengths):
    l = 0
    while(True):
        if num>=len(lengths):
            if num%2 == 0:
                num//=2
                l+=1
            else:
                num = (3*num+1)//2
                l+=2
        elif lengths[num] != 0:
            return l + lengths[num]
        else:
            if num%2 == 0:
                num//=2
                l+=1
            else:
                num = (3*num+1)//2
                l+=2
            if num == 1:
                return l

for i in range(2,1_000_001):
    lengths[i] = get_collatz_length(i, lengths)
print((lengths.index(max(lengths))))