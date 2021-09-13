import heapq
import copy
k, n = map(int, input().split())

arr = list(map(int, input().split()))

co = copy.deepcopy(arr)
sets = set()

heapq.heapify(co)
answer = 0

while answer <n:
    temp = heapq.heappop(co)
    if temp in sets:
        continue
    answer += 1
    sets.add(temp)
    for i in arr:
        heapq.heappush(co, i*temp)

print(temp)