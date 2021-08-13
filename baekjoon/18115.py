from collections import deque
n = int(input())

arr = list(range(n, 0, -1))

answer = deque()

data = list(map(int, input().split()))

for i in range(n-1,-1,-1):
    if data[i] == 1:
        answer.appendleft(arr.pop())
    if data[i] == 2:
        answer.insert(1,arr.pop())
    if data[i] == 3:
        answer.append(arr.pop())
print(' '.join(map(str,answer)))

    
