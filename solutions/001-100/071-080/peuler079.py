# Project Euler - 79
# Date: 12/07/2022

with open("lib\\001-100\\peuler_resource079.txt","r") as file:
    entries = []
    for row in file:
        entries.append(row[:-1])

print(entries)
col1, col2 ,col3 = set(),set(),set()
cols = [col1,col2,col3]
used = []

for i in range(len(entries)):
    for j in range(len(entries[i])):
        cols[j].add(entries[i][j])

total_set = col1.union(col2)
total_set = total_set.union(col3)

def find_candidates(total_set,cols, used):
    not_used_set = total_set - set(used)
    if not_used_set == set():
        return set()
    candidates = not_used_set - cols[2]
    candidates = candidates - cols[1]
    if candidates != set():
        return candidates
    candidates = not_used_set - cols[2]
    if candidates != set():
        return candidates
    return not_used_set

def eliminate(num1,num2, entries):
    for entry in entries:
        if entry[1:] == num1+num2 or entry[:2] == num1+num2:
            return num2
        elif entry[1:] == num2+num1 or entry[:2] == num2+num1:
            return num1
    return None
while(True):
    temp = find_candidates(total_set, cols, used)
    if len(used) == len(total_set):
        print(used)
        break
    if len(temp) > 1:
        temp = list(temp)
        while(True):
            to_elim = eliminate(temp[0],temp[1],entries)
            if to_elim == None:
                print(temp[0],temp[1])
                temp[0],temp[2] = temp[2], temp[0]
            else:
                temp.remove(to_elim)
                if len(temp) == 1:
                    used.append(temp[0])
                    break
    else:
        for var in temp:
            used.append(var)
