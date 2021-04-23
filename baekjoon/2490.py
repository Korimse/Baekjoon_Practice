a = ['E', 'A', 'B', 'C', 'D']
for _ in range(3):
    yoot = list(map(int, input().split()))

    cnt = yoot.count(0)
    print(a[cnt])
