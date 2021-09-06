a, b, c = map(int, input().split())

result = 0

dic = {}

for i in [a,b,c]:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

dic = sorted(dic.items(), key=lambda x : (-x[1], -x[0]))
if dic[0][1] == 3:
    result = 10000 + dic[0][0]*1000
elif dic[0][1] == 2:
    result = 1000 + dic[0][0]* 100
else:
    result = dic[0][0]*100
print(result)