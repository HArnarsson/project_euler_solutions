# Project Euler - 26
# Date: 01/06/2022

def find_decimal_repr(numerator,denominator):
    result = ""
    map = {}
    remainder = numerator%denominator
    while((remainder!=0) and (remainder not in map)):
        map[remainder] = len(result)
        remainder*=10
        result_temp = remainder//denominator
        result += str(result_temp)
        remainder = remainder%denominator
    if remainder == 0:
        return ""
    else:
        return result[map[remainder]:]

max_len = 0
max_d = 0
for d in range(1,1000):
    if len(find_decimal_repr(1,d))>max_len:
        max_len = len(find_decimal_repr(1,d))
        max_d = d

print(max_d)