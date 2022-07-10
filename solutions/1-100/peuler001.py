#Project Euler - 1
#Date: 04/05/2022
sum = 0
for i in range(1,1000):
    if i % 3 == 0:
        sum+=i
    elif i % 5 == 0:
        sum+=i
print(sum)        