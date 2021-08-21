import sys
input = sys.stdin.readline

n = int(input())
data = {}
for _ in range(n):
    book = input().rstrip()
    if book in data:
        data[book] += 1
    else:
        data[book] = 1

max_key = sorted(data.items(), key = lambda x : (-x[1], x[0]))
print(max_key[0][0])