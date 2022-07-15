# Project Euler - 33
# Date: 02/06/2022

from math import gcd
listy = []
for i in range(10,101):
    for j in range(10,i):
        numerator = str(j)
        denominator = str(i)
        for digit in numerator:
            if digit in denominator and digit !="0" and denominator[1] != "0":
                numerator = numerator.replace(digit, '',1)
                denominator = denominator.replace(digit,'',1)
                if j/i == int(numerator)/int(denominator):
                    listy.append([j,i])
                break
top = 1
bottom = 1
for i in range(len(listy)):
    top = top*listy[i][0]
    bottom *= listy[i][1]
print(bottom//gcd(top,bottom))