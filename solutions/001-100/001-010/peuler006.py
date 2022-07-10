#Project Euler - 6
#Date: 04/05/2022

sum_squares = 0
sum_squared = 0

for i in range(1,101):
    sum_squares += i**2
    sum_squared += i

sum_squared = sum_squared**2

print(sum_squared - sum_squares)