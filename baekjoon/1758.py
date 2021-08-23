n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

total = 0
arr.sort(reverse=True)
for i in range(len(arr)):
    if arr[i]-i <= 0:
        break
    else:
        total += arr[i] - i
print(total)