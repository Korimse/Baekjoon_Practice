n, c = map(int, input().split())

arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()

answer = 0

left = arr[1] - arr[0]
right = arr[-1] - arr[0]

while left <= right:
    mid = (left + right) // 2
    old = arr[0]
    count = 1

    for i in range(1, len(arr)):
        if arr[i] >= old + mid:
            count += 1
            old = arr[i]
    
    if count >= c:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1
print(answer)