import math
import sys
input = sys.stdin.readline

def get_distance(po1, po2):
    a = po1[0] - po2[0]
    b = po1[1] - po2[1]
    return math.sqrt((a*a) + (b*b))

def find_parent(parent, x):
    if parent[x] == x:
        return x
    return find_parent(parent, parent[x])

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def get_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
        return True
    else:
        return False

n, m = map(int, input().split())
location = []
edges = []
parent = {}
for i in range(n):
    a, b = map(int, input().split())
    location.append((a,b))

for i in range(len(location)-1):
    for j in range(i+1, len(location)):
        edges.append((i+1, j+1, get_distance(location[i], location[j])))

for i in range(1, n+1):
    parent[i] = i

for i in range(m):
    a, b = map(int, input().split())
    union(parent, a, b)

edges.sort(key = lambda x: x[2])

result = 0
for a, b, dist in edges:
    if not get_parent(parent, a, b):
        union(parent, a, b)
        result += dist

print("%0.2f" %result)