n = int(input())

arr = []
for i in range(n):
    arr.append(input())

count = 0
for ar in arr:
    stack = []
    for i in range(len(ar)):
        if stack and stack[-1] == ar[i]:
            stack.pop()
            continue
        stack.append(ar[i])
    if not stack:
        count+=1
print(count)