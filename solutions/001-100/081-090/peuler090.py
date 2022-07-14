# Project Euler - 90
# Date: 14/07/2022

from itertools import combinations

def can_make_all_squares(set1:set,set2:set):
    if 6 in set1:
        set1.add(9)
    if 9 in set1:
        set1.add(6)
    if 6 in set2:
        set2.add(9)
    if 9 in set2:
        set2.add(6)
    union = set1.union(set2)
    union.discard(7)
    if union != {0,1,2,3,4,5,6,8,9}:
        return False
    s = [[0,1],[0,4],[0,9],[1,6],[2,5],[3,6],[4,9],[6,4],[8,1]]
    to_return = True
    for i in range(len(s)):
        if not((s[i][0] in set1 and s[i][1] in set2) or (s[i][1] in set1 and s[i][0] in set2)):
            to_return = False
            break
    return to_return

digits = list(range(10))
combs = list(combinations(digits,6))
dice = list(combinations(combs,2))

c=0
for set1,set2 in dice:
    set1 = set(set1)
    set2 = set(set2)
    c += int(can_make_all_squares(set1,set2))
print(c)
