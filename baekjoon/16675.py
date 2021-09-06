ml, mr, tl, tr = map(str, input().split())
isTrue = 0

def play(a, b):
    if a == 'R':
        if b == 'S':
            return True
        else:
            return False
    elif a == 'P':
        if b == 'R':
            return True
        else:
            return False
    elif a == 'S':
        if b == 'P':
            return True
        else:
            return False

for a in [ml, mr]:
    count = 0
    for b in [tl, tr]:
        if play(a, b):
            count += 1
    if count == 2:
        isTrue = 1
        break

if isTrue == 0:
    for a in [tl, tr]:
        count = 0
        for b in [ml, mr]:
            if play(a, b):
                count += 1
        if count == 2:
            isTrue = 2
            break

if isTrue == 1:
    print("MS")
elif isTrue == 2:
    print("TK")
else:
    print("?")