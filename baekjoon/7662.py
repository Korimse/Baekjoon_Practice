import heapq
import sys

input = sys.stdin.readline

T = int(input())

result = []
for _ in range(T):
    k = int(input())
    maxh = []
    minh = []
    visited = [False]*1_000_001
    for i in range(k):
        string = input()
        s, n = string.split()
        print(s, n)
        if s == 'I':
            heapq.heappush(maxh, (-int(n), i))
            heapq.heappush(minh, (int(n), i))
            visited[i] = True
        elif s == 'D':
            if n == '1':
                while maxh and not visited[maxh[0][1]]:
                    heapq.heappop(maxh)
                if maxh:
                    visited[maxh[0][1]] = False
                    heapq.heappop(maxh)
            elif n == '-1':
                while minh and not visited[minh[0][1]]:
                    heapq.heappop(minh)
                if minh:
                    visited[minh[0][1]] = False
                    heapq.heappop(minh)
    while minh and not visited[minh[0][1]]:
        heapq.heappop(minh)
    while maxh and not visited[maxh[0][1]]:
        heapq.heappop(maxh)
    result.append(f'{-maxh[0][0]} {minh[0][0]}' if maxh and minh else "EMPTY")
print('\n'.join(result))