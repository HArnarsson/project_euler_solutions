# Project Euler - 84
# Date: 13/07/2022

from time import time
from random import choice, shuffle
def throw_dice():
    lst = [1,2,3,4]
    return choice(lst),choice(lst)

def next_R(pos):
    if pos%40 < 5 or pos%40>35:
        return 5
    elif 5<pos%40<15:
        return 15
    elif 15<pos%40<25:
        return 25 
    elif 25<pos%40<35:
        return 35 

def next_U(pos):
    if pos>28 or pos<12:
        return 12
    elif 12<pos<28:
        return 28

def go_2_jail(pos):
    return 10

def community_chest(pos, cc_pile:list):
    card = cc_pile.pop(0)
    cc_pile.append(card)
    if card == 0:
        return 0
    elif card == 1:
        return 10
    else: 
        return pos

def chance(pos, ch_pile):
    card = ch_pile.pop(0)
    ch_pile.append(card)
    if card == 0:
        return 0
    elif card == 1:
        return 10
    elif card == 2:
        return 11
    elif card == 3:
        return 24
    elif card == 4:
        return 39
    elif card == 5:
        return 5
    elif card == 6 or card == 7:
        return next_R(pos)
    elif card == 8:
        return next_U(pos)
    elif card == 9:
        return pos-3
    else:
        return pos

def play_game(num_throws):
    counting_array = [0]*40
    cc_pile = list(range(16))
    shuffle(cc_pile)
    ch_pile = list(range(16))
    shuffle(ch_pile)
    pos = 0
    count = 0
    i = 0
    while(i<num_throws):
        a,b = throw_dice()
        # if a == b:
        #     count += 1
        # else:
        #     count = 0
        # if count == 3:
        #     pos = go_2_jail(pos)
        pos = (pos+a+b)%40
        while(True):
            if pos in [2,17,33]:
                pos = community_chest(pos, cc_pile)
                if pos in [2,17,33]:
                    break
            elif pos in [7,22,36]:
                pos = chance(pos, ch_pile)
                if pos in [7,22,36]:
                    break
            elif pos == 30:
                pos = go_2_jail(pos)
            else:
                break
        counting_array[pos]+=1
        i+=1
    return counting_array

start = time()
counting_array = [0]*40
for _ in range(100000):
    temp = play_game(100)
    for i in range(len(temp)):
        counting_array[i] += temp[i]

sorted_array = sorted(counting_array,reverse=True)
lst = []
print(counting_array)
for i in range(3):
    lst.append(counting_array.index(sorted_array[i]))

print(lst)
print(time()-start)
