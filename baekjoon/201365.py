n = int(input())

data = list(input().rstrip())
data.append('A')
Bcount = 1
Rcount = 1

for i in range(n):
    if data[i] == 'B':
        continue
    elif data[i] == 'R':
        if data[i+1] != 'R':
            Bcount += 1
            continue
for i in range(n):
    if data[i] == 'R':
        continue
    elif data[i] == 'B':
        if data[i+1] != 'B':
            Rcount += 1
            continue
print(min(Bcount, Rcount))