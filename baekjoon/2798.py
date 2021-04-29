from itertools import combinations

n, m = map(int, input().split())

arr = list(map(int, input().split()))

ar = combinations(arr, 3)
maxv = 0
for a in ar:
    if sum(a) <= m:
        maxv = max(maxv, sum(a))
print(maxv)