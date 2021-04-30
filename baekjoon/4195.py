t = int(input())

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    x,y = find(x), find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]

for _ in range(t):
    n = int(input())

    parent = dict()
    number = dict()

    for i in range(n):
        x,y = input().split(' ')

        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        
        union(x, y)
        print(number[find(x)])