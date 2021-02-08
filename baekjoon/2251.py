from collections import deque
import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())
answer = [0]*201
visited = [[0]*201 for i in range(201)]

queue = deque()
queue.append([0,0,c])
def bfs():
    while queue:
        x, y, z = queue.popleft()
        if visited[x][y] == 1: continue
        visited[x][y] = 1
        if x == 0: answer[z] = 1
        if x + y > b: queue.append([x + y - b, b, z])
        else: queue.append([0, x + y, z])
        if x + z > c: queue.append([x + z - c, y, c])
        else: queue.append([0, y, x + z])
        if y + x > a: queue.append([a, y + x - a, z])
        else: queue.append([y + x, 0, z])
        if y + z > c: queue.append([x, y + z - c, c])
        else: queue.append([x, 0, y + z])
        if z + x > a: queue.append([a, y, z + x - a])
        else: queue.append([z + x, y, 0])
        if z + y > b: queue.append([x, b, z + y - b])
        else: queue.append([x, z + y, 0])

bfs()
for i in range(201):
  if answer[i]:
    print(i, end = " ")
