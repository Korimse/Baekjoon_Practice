n = int(input())

arr = list(map(int, input().split()))

arr.sort()
su = 0
for i in range(n):
  if su +1 >= arr[i]:
    su += arr[i]
  else:
    break
print(su+1)