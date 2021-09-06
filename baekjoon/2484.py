n = int(input())
answer = []
for i in range(n):
    a, b, c, d = map(int, input().split())

    result = 0

    dic = {}

    for i in [a,b,c,d]:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    dic = sorted(dic.items(), key=lambda x : (-x[1], -x[0]))
    if dic[0][1] == 4:
        result = 50000 + dic[0][0]*5000
    elif dic[0][1] == 3:
        result = 10000 + dic[0][0]*1000
    elif dic[0][1] == 2:
        if dic[1][1] == 2:
            result = 2000 + dic[0][0]*500 + dic[1][0]*500
        else:
            result = 1000 + dic[0][0]* 100
    else:
        result = dic[0][0]*100
    answer.append(result)
print(max(answer))