# Project Euler - 38
# Date: 02/06/2022

def is_pandigital(num):
    stringy = str(num)
    nums = ['1','2','3','4','5','6','7','8','9']
    for digit in stringy:
        if digit in nums:
            nums.remove(digit)
            continue
        else:
            return False
    if nums == []:
        return True
    else:
        return False

def generate_nine_digit_nums(limit):
    n = 2
    listy =[]
    while n<limit:
        stringy = ""
        i = 1
        while len(stringy)<=9:
            if len(stringy)==9:
                listy.append(stringy)
                stringy = ""
            else:
                stringy += str(n*i)
            i+=1
        n+=1
    return listy

pandigital_nums = []
nums = (generate_nine_digit_nums(10**4))
for num in nums:
    if is_pandigital(num):
        pandigital_nums.append(num)

print(max(pandigital_nums))