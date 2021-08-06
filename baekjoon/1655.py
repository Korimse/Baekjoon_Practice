import heapq
import sys

input = sys.stdin.readline

n = int(input())

left_heap = []
right_heap = []

for i in range(n):
    num = int(input())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, (-num, num))
    else:
        heapq.heappush(right_heap, (num, num))
    
    if len(left_heap) > 0 and len(right_heap) > 0 and left_heap[0][1] > right_heap[0][1]:
        left_v = heapq.heappop(left_heap)[1]
        right_v = heapq.heappop(right_heap)[1]
        heapq.heappush(left_heap, (-right_v, right_v))
        heapq.heappush(right_heap, (left_v, left_v))

    print(left_heap[0][1])
