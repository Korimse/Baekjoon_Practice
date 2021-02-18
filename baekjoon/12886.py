from collections import deque, defaultdict
stones = list(map(int, input().split()))
visited = defaultdict(bool)
total = sum(stones)
def bfs():
    q = deque([stones])
    visited[tuple(stones)] = True
    while q:
        a,b,c = q.popleft()
        if a==b==c: 
            return 1
        for x,y in ((a,b),(a,c),(b,c)):
            if x == y: continue
            elif x < y:
                y -= x
                x += x
            elif x > y:
                x -= y
                y += y
            z = total-x-y
            if not visited[(x,y,z)] :
                visited[(x,y,z)] = True
                q.append([x,y,z])
    return 0
if total%3 != 0: print(0)
else:
    print(bfs())
