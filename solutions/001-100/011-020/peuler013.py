# Project Euler - 13
# Date: 16/05/2022

from urllib.request import urlopen
from re import findall

with urlopen('https://projecteuler.net/minimal=13') as response:
    html = response.read().decode()

regex = "\d+"
nums = findall(regex, html)
nums = nums[1:]
nums = [int(num) for num in nums]
summa = 0
for num in nums:
    summa+=num

print(str(summa)[:10])