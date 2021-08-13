import sys

input = sys.stdin.readline
n, m = map(int, input().split())


dic = {}
dicArray = {}
for i in range(1,n+1):
    s = input().strip()
    dic[s] = i
    dicArray[i] = s

for i in range(m):
    data = input().rstrip()
    if data.isdigit():
        print(dicArray[int(data)])
    else:
        print(dic[data])
