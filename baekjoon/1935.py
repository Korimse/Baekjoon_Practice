from collections import deque

n = int(input())

s = input()

arr = []
for i in range(n):
    arr.append(float(input()))

stack = []

for i in range(len(s)):
    if "A"<=s[i]<="Z":
        stack.append(arr[ord(s[i])-65])
    else:
        b = stack.pop()
        a = stack.pop()
        if s[i] == '+':
            stack.append(a+b)
        elif s[i] == '-':
            stack.append(a-b)
        elif s[i] == '*':
            stack.append(a*b)
        elif s[i] == '/':
            stack.append(a/b)
print(f"{stack[0]:.2f}")