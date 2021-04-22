t = int(input())

for _ in range(t):
    answer = 0

    s = input()
    tmp = 0
    for i in range(len(s)):
        if s[i] == 'X':
            tmp = 0
        else:
            tmp += 1
        answer += tmp
    
    print(answer)