from itertools import combinations
n = int(input())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def check(lists):
    global answer
    sets = set()
    for l in lists:
        sets.add((l[0], l[1]))
        for i in range(4):
            nx = l[0] + dx[i]
            ny = l[1] + dy[i]
            sets.add((nx, ny))
    if len(sets) == 15:
        sums = 0
        for x, y in sets:
            sums += graph[x][y]
        answer = min(answer, sums)
    else:
        return

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

can = []
for i in range(1, n-1):
    for j in range(1, n-1):
        can.append((i,j))

answer = int(1e9)

for li in combinations(can, 3):
    check(li)
    
print(answer)