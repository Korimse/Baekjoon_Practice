n = int(input())
nlist = list(map(int, input().split()))

m = int(input())
mlist = list(map(int, input().split()))

def binary_search(a, start, end, target):
    while start <= end:
        mid = (start+end)//2
        if target == a[mid]:
            return True
        elif target < a[mid]:
            end = mid -1
        else:
            start = mid + 1
    return False
nlist.sort()
for k in mlist:
    isTrue = binary_search(nlist, 0, n-1, k)
    if isTrue == True:
        print(1)
    else:
        print(0)