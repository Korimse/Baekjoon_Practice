answer = []
def bfs(arr, i, target):
    if arr >= target:
        if arr == target:
            answer.append(i)
        return
    
    bfs(arr*2, i+1, target)
    bfs(arr*10 + 1, i+1, target)

a, t = map(int, input().split())
bfs(a, 1, t)

if answer:
    print(answer[0])
else:
    print(-1)