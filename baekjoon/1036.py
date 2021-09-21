k, d, n = map(str, input().split())

map = [[0 for _ in range(8)] for _ in range(8)]

column = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
row = [8,7,6,5,4,3,2,1]
direct = {'R':(0,1), 'L':(0,-1), 'B':(1,0), 'T':(-1,0), 'RT':(-1,1), 'LT':(-1,-1), 'RB':(1,1), 'LB':(1,-1)}

ki = row.index(int(k[1]))
kj = column.index(k[0])

di = row.index(int(d[1]))
dj = column.index(d[0])

map[ki][kj] = 1
map[di][dj] = 2

for i in range(int(n)):
    order = input()
    if order in direct:
        i, j = direct[order]
    
    nx = ki+i
    ny = kj+j

    if 0<=nx<8 and 0<=ny<8:
        if map[nx][ny] == 0:
            map[ki][kj] = 0
            map[nx][ny] = 1
            ki = nx
            kj = ny
        elif map[nx][ny] == 2:
            nx2 = di+i
            ny2 = dj+j

            if 0<=nx2<8 and 0<=ny2<8:
                map[di][dj] = 0
                map[nx2][ny2] = 2
                di = nx2
                dj = ny2

                map[ki][kj] = 0
                map[nx][ny] = 1
                ki = nx
                kj = ny


for i in range(8):
    for j in range(8):
        if map[i][j] == 1:
            ki = i
            kj = j
        if map[i][j] == 2:
            di = i
            dj = j
print(column[kj]+str(row[ki]))
print(column[dj]+str(row[di]))