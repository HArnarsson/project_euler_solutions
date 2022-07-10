# Project Euler - 41
# Date: 03/06/20222

def is_pandigital(num):
    stringy = str(num)
    nums = ['1','2','3','4','5','6','7','8','9']
    nums = nums[:len(stringy)]
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

def is_prime(n):
    if n==1:
        return False
    if n%5 == 0 and n != 5:
        return False
    for i in range(2,int(abs(n)**0.5)+1):
        if n%i == 0:
            return False
    return True
def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]

    p = 2
    while (p * p <= num):

        if (prime[p] == True):
 
            # Updating all multiples of p
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
 
    for p in range(2, num+1):
        if prime[p]:
            yield p
pandigital_nums = []
for i in range(3,10**7,2):
    if is_pandigital(i):
        pandigital_nums.append(i)

for num in pandigital_nums:
    if is_prime(num):
        biggest_num = num
print(biggest_num)
#ath hér er mikilvægt að athuga að einungis tölur sem eru 4 eða 7 stafa langar geta uppfyllt skilyrðið sbr. þversumma og deilanlegt með 3