st = input()

stack = []
isTrue = True
temp = 1
ans = 0
for i in range(len(st)):
    if st[i] == '(':
        stack.append(st[i])
        temp *= 2
    elif st[i] == '[':
        stack.append(st[i])
        temp *= 3
    elif st[i] == ')':
        if stack:
            if st[i-1] == '(':
                ans += temp
            if stack[-1] == '(':
                stack.pop()
                temp //=2
        else:
            isTrue = False
            break
    elif st[i] == ']':
        if stack:
            if st[i-1] == '[':
                ans += temp
            if stack[-1] == '[':
                stack.pop()
                temp //=3
        else:
            isTrue = False
            break

if isTrue and not stack:
    print(ans)
else:
    print(0)