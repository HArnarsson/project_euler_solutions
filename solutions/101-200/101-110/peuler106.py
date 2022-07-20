# Project Euler - 106
# Date: 20/07/2022

from math import comb

# Dyck words!

# https://en.wikipedia.org/wiki/Catalan_number

# First of all it is obvious that the subset pairs need to be of equal length
# For a given dyck word we can find Y such that X appears before Y, for example
# Look at the set {a1,a2,a3,a4,a5,a6} such that a1<a2<a3<a4<a5<a6, a X represents one of these a-s chosen into set 1 and Y one chosen into set2
# We need to check equality if we do not have a dyck word. 
# Another way to think of it is if we have a dyck word, the sum of X-s is always smaller than the sum of Y-s
# Finally, if we need to check for subset pairs whose union is not the whole set i.e. length 2 in a set of 6, we still only need to check for the total 
# pairs - dyck words but we multiply by comb(6,2*2) since we are choosing 4 numbers to make a dyck word from out of 6.
# In general this means that if we have a subset pair of length m and a set of length n the number of words we do NOT need to check is num(dyckwords)*comb(n,2*m)
# From the wikipedia article referenced above we have that the number of dyck words of length m is the Catalan number number m which is given by comb(2*m,m)//(m+1)
# or alternatively, (faster to compute) the product of (n+k)/k from k = 2 to n
# Now all that is left is to find the total number of pairs. As mentioned above we only need to check where the pairs are of equal length
# Say we have a set of length n and want a set of length m. To choose the first set we have comb(n,m), for the second set we have comb(n-m,m) since we have already
# taken m numbers from the set. Note that we are double counting here since choosing for example a4a5a6 and then a1a2a3 is equivalent to a1a2a3 and then a4a5a6, therefore,
# ur total number of pairs is comb(n,m)*comb(n-m,m)//2. Now we are ready to solve the problem.

def catalan(m):
    p = 1
    for k in range(2,m+1):
        p*=(m+k)/k
    return round(p)

def num_nice_pairs(n,m):
    return comb(n,m)*comb(n-m,m)//2 - catalan(m)*comb(n,2*m)

def num_need_equality_check(n):
    s = 0
    for m in range(2,n//2+1):
        s += num_nice_pairs(n,m)
    return s

print((num_need_equality_check(12)))
