# Project Euler - 40
# Date: 03/06/2022

stringy = ""
for i in range(10**6):
    stringy += str(i)

print(int(stringy[1])*int(stringy[10])*int(stringy[100])*int(stringy[1000])*int(stringy[10000])*int(stringy[100000])*int(stringy[1000000]))