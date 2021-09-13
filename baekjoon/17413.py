s = input()

isTag = False
words = ''
answer = ''
for i in range(len(s)):
    if isTag == True:
        answer += s[i]

    if isTag == False and (s[i] != '<' and s[i] != '>'):
        words += s[i]
    
    if s[i] == '<':
        if words:
            word = words.split(" ")
            for w in word:
                answer += w[::-1] + ' '
            answer = answer[0:-1]
            words = ''
        isTag = True
        answer += s[i]

    if s[i] == '>':
        isTag = False
if words:
    word = words.split(" ")
    for w in word:
        answer += w[::-1] + ' '
    answer = answer[0:-1]

print(answer)