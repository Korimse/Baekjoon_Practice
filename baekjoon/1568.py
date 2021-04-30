n = int(input())

i = 1
sec = 0
while n > 0:
    if n >= i:
        n -= i
        i += 1
        sec += 1
    else:
        i = 1

print(sec)
