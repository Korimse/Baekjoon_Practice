n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

temp = []
sumv = 0
for i in range(len(arr)):
    if i % 3 == 2:
        temp.append(arr[i])
        print(temp)
        temp.sort(reverse=True)
        sumv += temp[0]+temp[1]
        temp = []
    else:
        temp.append(arr[i])
if temp:
    sumv += sum(temp)
print(sumv)