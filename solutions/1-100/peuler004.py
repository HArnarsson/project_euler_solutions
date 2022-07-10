#Project Euler - 4
#Date: 04/05/2022

# This is shit
def is_palindrome(number:int or str) -> bool:
    number = str(number)
    if len(number) % 2 == 0:
        if number[0:len(number)//2] == number[len(number):len(number)//2-1:-1]:
            return True
        else:
            return False
    elif len(number) % 2 != 0:
        if number[0:len(number)//2] == number[len(number):len(number)//2:-1]:
            return True
        else:
            return False
    else:
        return False

#This was added by Hilmir after he stopped being an idiot

def is_palindrome(number):
    number = str(number)
    return number == number[::-1]
    
lst = []
for i in range(100,1000):
    for j in range(100,1000):
        if is_palindrome(i*j):
            lst.append(i*j)
print(max(lst))