with open('peuler_resource018.txt','r') as triangle:
    rows = []
    for row in triangle:
        rows.append(row)
rows = [rows[i] + '0'*len(rows[-1]-i) for i in range(len(rows))]
print(rows)