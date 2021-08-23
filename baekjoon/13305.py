n = int(input())

road = list(map(int, input().split()))
gas = list(map(int, input().split()))

minv = 1000000001
total = 0

for i in range(n-1):
    if i == 0:
        total += road[0]*gas[0]
        minv = min(minv, gas[i])
    else:
        minv = min(minv, gas[i])
        total += road[i]*minv
print(total)