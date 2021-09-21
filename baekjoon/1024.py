from collections import deque

n, l = map(int, input().split())
answer = []

def solve(arr, n, i):
    global answer
    if sum(arr) == n:
        print(arr)
        arr.append(i+1)
        solve(arr, n,i)
        return

    if i >= 100:
        print(-1)
        return
    if sum(arr) < n:
        arr.append(i+1)
        solve(arr, n, i+1)
    elif sum(arr) > n:
        arr.popleft()
        solve(arr, n, i+1)


queue = deque()
solve(queue, n, 0)
print(answer)