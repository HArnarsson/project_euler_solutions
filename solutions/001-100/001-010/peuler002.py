#Project Euler - 2
#Date: 04/05/2022

n=2
fibonacci_nums = [1,2]
while True:
    num = fibonacci_nums[n-2] + fibonacci_nums[n-1]
    if num >= 4000000:
        break
    else:
        fibonacci_nums.append(num)
    n+=1

sum=0
for number in fibonacci_nums:
    if number % 2 == 0:
        sum+= number
print(sum)
