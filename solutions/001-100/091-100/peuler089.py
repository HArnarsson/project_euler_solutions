# Project Euler - 89
# Date 14/07/2022

import re
    
with open("lib\\001-100\\peuler_resource089.txt","r") as file:
    roman_nums = ""
    for roman_num in file:
        roman_nums += roman_num

regex = "DCCCC|CCCC|LXXXX|XXXX|VIIII|IIII"
shortening_opportunities = re.sub(regex, "00", roman_nums)
print(len(roman_nums)-len(shortening_opportunities))
