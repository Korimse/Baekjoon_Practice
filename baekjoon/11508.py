n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

temp = []
sumv = 0
for i in range(len(arr)):
    if i % 3 == 2:
        continue
    else:
        sumv += arr[i]

print(sumv)