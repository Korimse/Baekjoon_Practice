n = int(input())
arr = {}
for _ in range(n):
    name = input().rstrip()
    if name in arr:
        arr[name] += 1
    else:
        arr[name] = 1

for _ in range(n-1):
    name = input().rstrip()
    arr[name] -= 1

for ar in arr:
    if arr[ar]:
        print(ar)
        break