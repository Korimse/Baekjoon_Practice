import heapq

n = int(input())
arr = []
for _ in range(n):
    d = int(input())

    if d != 0:
        heapq.heappush(arr, d)
    else:
        if arr:
            print(arr[0])
            heapq.heappop(arr)
        else:
            print(0)
