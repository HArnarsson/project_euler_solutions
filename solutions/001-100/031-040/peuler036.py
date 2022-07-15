# Project Euler - 36
# Date: 02/06/2022

def decimal_to_binary(num:int):
    return bin(num)[2:]

def is_palindrome(num):
    num = str(num)
    if num == num[::-1]:
        return True
    else:
        return False

summa = 0
for i in range(1,10**6):
    if is_palindrome(i) and is_palindrome(decimal_to_binary(i)):
        summa += i
print(summa)