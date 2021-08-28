from collections import deque

MAX = 100001
n, k = map(int, input().split())

array = [0]*MAX

def bfs():
    q = deque([n])
    while q:
        now = q.popleft()
        if now == k:
            return array[now]
        for next in (now-1, now+1, now*2):
            if 0 <= next < MAX and not array[next]:
                array[next] = array[now]+1
                q.append(next)
print(bfs())