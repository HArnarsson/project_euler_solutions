# Project Euler - 22
# Date: 01/06/2022

from re import findall
filepath = "lib\\001-100\\peuler_resource022.txt"
names = ""
with open(filepath, 'r', encoding='utf-8') as file:
    for row in file:
        names += row
regex = "(?i)\"\w+\""
listy = findall(regex, names)

for i in range(len(listy)):
    listy[i] = listy[i][1:]
    listy[i] = listy[i][:-1]
listy.sort()

def find_score(index, name):
    summa = 0
    for i in range(len(name)):
        summa += ord(name[i])-64
    return summa*index

summa = 0
for i in range(len(listy)):
    summa += find_score(i+1, listy[i])
print(summa)