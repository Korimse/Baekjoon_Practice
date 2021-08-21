time = list(map(str,input().split()))
s = []
names = []
result = set()
for t in time:
    temp = t.split(":")
    s.append(int(temp[0]) * 60 + int(temp[1]))

for _ in range(20):
    string = input()
    if string == '':
        break

    strr = string.split(" ")
    tt = strr[0].split(":")
    time = int(tt[0])*60 + int(tt[1])
    if time <= s[0]:
        names.append(strr[1])
    
    elif s[1]<=time <= s[2]:
        if strr[1] in names:
            result.add(strr[1])
print(len(result))