# Project Euler - 18
# Date: 31/05/2022

with open('lib\\001-100\\peuler_resource018.txt','r') as triangle:
    rows = []
    for row in triangle:
        row = row.split()
        rows.append(row)
rows = [rows[i] + ['0']*(len(rows[-1])-i-1) for i in range(len(rows))]
for i in range(len(rows)):
    for j in range(len(rows[i])):
        rows[i][j] = int(rows[i][j])

def find_max_path(triangle):
    for i in range(len(triangle)-2,-1,-1):
        for j in range(len(triangle[i])-(14-i)):
            triangle[i][j]+=max(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]
print(find_max_path(rows))
