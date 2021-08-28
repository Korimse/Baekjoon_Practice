import sys
input = sys.stdin.readline

def quickSort(data):
    if len(data) <= 1:
        return data
    
    pivot = data[0]

    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]

    return quickSort(left) + [pivot] + quickSort(right)

n = int(input())
data = []
for i in range(n):
    t = int(input())
    data.append(t)
    
result = quickSort(data)

for r in result:
    print(r)