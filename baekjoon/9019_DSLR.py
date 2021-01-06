from collections import deque
import sys
input = sys.stdin.readline
def bfs():
  queue = deque()
  queue.append((a, ""))
  while queue:
    num, result = queue.popleft()
    D = (num*2)%10000
    if D == b:
      return result + "D"
    elif visited[D] == 0:
      visited[D] = 1
      queue.append((D, result+"D"))
    if num == 0:
      S = 9999
    else:
      S = num - 1
    if S == b:
      return result + "S"
    elif visited[S] == 0:
      visited[S] = 1
      queue.append((S, result + "S"))
    L = int(num%1000*10 + num/1000)
    if L == b:
      return result + "L"
    elif visited[L] == 0:
      visited[L] = 1
      queue.append((L, result + "L"))
    R = int(num%10*1000 + num//10)
    if R == b:
      return result + "R"
    elif visited[R] == 0:
      visited[R]= 1
      queue.append((R, result + "R"))

n = int(input())
for i in range(n):
  a, b = map(int, input().split())
  visited = [0 for _ in range(10000)]
  print(bfs())