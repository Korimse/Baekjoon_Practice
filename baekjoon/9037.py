import copy
t = int(input())
for i in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    for i in range(n):
            if arr[i] % 2 != 0:
                arr[i] += 1

    cnt = 0
    while arr.count(arr[0]) != n:
        
        for i in range(n):
            arr[i] /= 2
        temp = copy.deepcopy(arr)
        for i in range(n):
            if i == 0:
                arr[i] += temp[-1]
            else:
                arr[i] += temp[i-1]

        for i in range(n):
            if arr[i] % 2 != 0:
                arr[i] += 1
        cnt += 1
    print(cnt)
