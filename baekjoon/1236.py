n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(input())
row = [0]*n
column = [0]*m
for i in range(n):
    for j in range(m):
        if array[i][j] == 'X':
            row[i] = 1
            column[j] = 1

rowc = 0
for i in range(n):
    if row[i] == 0:
        rowc += 1

colc = 0
for i in range(m):
    if column[i] == 0:
        colc += 1
print(max(rowc, colc))