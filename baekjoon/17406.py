import copy
n, m, k = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

ro = []
for i in range(k):
    ro.append(list(map(int, input().split())))
dx = [1,0,-1,0]
dy = [0,-1,0,1]
ans = 100000

def value(arr):
    return min([sum(i) for i in arr])


def convert(arr, ro1):
    r, c, s = ro1
    r, c = r-1, c-1
    newArr=copy.deepcopy(arr)
    for i in range(1, s+1):
        rr, cc = r-i, c+i
        for w in range(4):
            for d in range(i*2):
                rrr, ccc = rr + dx[w], cc + dy[w]
                newArr[rrr][ccc] = arr[rr][cc]
                rr, cc = rrr, ccc
    return newArr

def dfs(arr, q):
    global ans
    if sum(q) == k:
        ans = min(ans, value(arr))
    for i in range(k):
        if q[i]:
            continue
        newArr = convert(arr, ro[i])
        q[i] = 1
        dfs(newArr, q)
        q[i] = 0

dfs(graph, [0 for i in range(k)])
print(ans)