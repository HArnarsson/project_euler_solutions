# Project Euler - 98
# Date: 14/07/2022

# I don't like this piece of code at all, it is very ugly but it gets the job done in a reasonable amount of time

from collections import Counter
from math import sqrt

with open("lib\\001-100\\peuler_resource098.txt",'r') as file:
    for row in file:
        string = str(row)
words = string.split(',')
for word in range(len(words)):
    words[word] = words[word][1:-1]

def is_anagram(w1,w2):
    return Counter(w1) == Counter(w2)

all_pairs = []
for i in range(len(words)-1):
    for j in range(i+1,len(words)):
        if is_anagram(words[i],words[j]):
            all_pairs.append((words[i],words[j]))

def gen_squares(start,limit):
    n = int(sqrt(start))
    s = []
    while n**2<limit:
        s.append(str(n**2))
        n+=1
    return s

max_len = 9

max_square = 0
while(True):
    print(max_len)
    anagram_pairs=[]
    for pair in all_pairs:
        if len(pair[0]) == max_len:
            anagram_pairs.append(pair)
    if anagram_pairs == []:
        max_len-=1
        continue
    for anagram_pair in anagram_pairs:
        mapping = {}
        for letter in anagram_pair[0]:
            mapping[anagram_pair[0].index(letter)] = anagram_pair[1].index(letter)
            
        is_square = lambda n : int(sqrt(n))**2 == n
        s = gen_squares(10**(max_len-1),10**(max_len)+1)

        for square in s:
            sett = set()
            for dig in square:
                sett.add(dig)
            if len(sett) != len(square):
                continue
            new_square = [0]*len(str(square))
            for key in mapping:
                new_square[mapping[key]] = str(square)[key]
            n = 0
            for i in range(1,len(new_square)+1):
                n+=10**(i-1)*int(new_square[-i])
            if is_square(n) and len(str(n)) == len(square) and is_anagram(square,str(n)):
                if n>max_square:
                    max_square = n
                    teno = square
    try:
        print(max(max_square, teno))
        break
    except:
        max_len-=1
