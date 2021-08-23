n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

sumv = arr[0]

for i in range(1, n):
    sumv += arr[i]/2
print('%g' %sumv)