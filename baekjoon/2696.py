import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    data = []
    if n % 10 == 0:
        for _ in range(n // 10):
            data.extend(list(map(int, input().split())))
    else:
        for _ in range(n // 10 + 1):
            data.extend(list(map(int, input().split())))
    
    left, right = [], []
    middle = data[0]
    result = [middle]
    for i, v in enumerate(data[1:], 1):
        if v > middle:
            heapq.heappush(right, v)
        else:
            heapq.heappush(left, -v)
        if i % 2 == 0:
            if len(left) < len(right):
                heapq.heappush(left, -middle)
                middle = heapq.heappop(right)
            elif len(left) > len(right):
                heapq.heappush(right, middle)
                middle = -heapq.heappop(left)
            result.append(middle)
    print(len(result))
    for i in range(len(result)):
        if (i + 1) != 1 and (i + 1) % 10 == 1:
            print()
        print(result[i], end=' ')
    print()