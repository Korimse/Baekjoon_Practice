import heapq

n = int(input())
arr = []
for i in range(n):
    nums = list(map(int, input().split()))

    if not arr:
        for num in nums:
            heapq.heappush(arr, num)
    else:
        for num in nums:
            if arr[0] < num:
                heapq.heappop(arr)
                heapq.heappush(arr, num)

print(arr[0])