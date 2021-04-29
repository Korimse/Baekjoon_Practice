n = int(input())
for _ in range(n):
    string = input()
    answer = []
    stack = []
    for s in string:
        if s == '<':
            if len(answer) > 0:
                stack.append(answer.pop())
        elif s == '>':
            if len(stack) > 0:
                answer.append(stack.pop())
        elif s == '-':
            if len(answer) > 0:
                answer.pop()
        else:
            answer.append(s)
    answer.extend(reversed(stack))
    print(''.join(answer))