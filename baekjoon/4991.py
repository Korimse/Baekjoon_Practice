from collections import deque
from itertools import permutations

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(robot):
    queue = deque()
    queue.append(robot)
    visited = [[0]*(len(arr[0])) for _ in range(len(arr))]
    visited[robot[0]][robot[1]] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<len(arr) and 0<=ny<len(arr[0]) and visited[nx][ny] == 0:
                if arr[nx][ny] != 'x':
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    
    return visited


while True:
    m,n = map(int, input().split())
    if m == 0 and n == 0:
        break
    arr = []
    dirty = []
    isTrue = True
    for i in range(n):
        tmp = list(input())
        arr.append(tmp)
        for j in range(len(tmp)):
            if tmp[j] == 'o':
                robot = (i, j)
            elif tmp[j] == '*':
                dirty.append((i,j))

    cleaner = [0] * len(dirty)
    visited = bfs(robot)
    for i, d in enumerate(dirty):
        temp = visited[d[0]][d[1]]
        if temp == 0:
            print(-1)
            isTrue = False
            break
        cleaner[i] += temp - 1
    if isTrue:
        dists = [[0] * len(dirty) for _ in range(len(dirty))]
        for i in range(len(dirty) - 1):
            visited = bfs(dirty[i])
            for j in range(i+1, len(dirty)):
                dists[i][j] = visited[dirty[j][0]][dirty[j][1]]-1
                dists[j][i] = dists[i][j]
        answer = int(1e9)

        for li in permutations(range(len(dists))):
            temp = cleaner[li[0]]
            start = li[0]
            for idx in range(1, len(li)):
                end = li[idx]
                temp += dists[start][end]
                start = end
            answer = min(answer, temp)
        print("answer : ", answer)

