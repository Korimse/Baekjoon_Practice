T = int(input())

def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        middle = (left + right) //2
        if arr[middle] == target:
            return 1
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return 0

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    m = int(input())
    data = list(map(int, input().split()))
    for d in data:
        print(binary_search(arr, d))