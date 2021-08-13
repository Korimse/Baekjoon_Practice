from itertools import combinations
import copy
s = input()

stack = []

arr = []
answer = []
for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    elif s[i] == ')':
        startIdx = stack.pop()
        endIdx = i
        arr.append((startIdx, endIdx))

c = [i for i in s]
for i in range(1, len(arr)+1):
    for j in combinations(arr, i):
        sc = copy.copy(c)
        for a, b in j:
            sc[a] = ''
            sc[b] = ''
        answer.append(''.join(sc))
answer = sorted(set(answer))
for i in answer:
    print(i)