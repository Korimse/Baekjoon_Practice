from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(n, m):
    queue = deque()
    count = 0
    queue.append((0,0))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[x][y] > arr[nx][ny]:
                    queue.append((nx,ny))
                    if nx == (n-1) and ny == (m-1):
                        count += 1
    return count

n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

print(bfs(n,m))