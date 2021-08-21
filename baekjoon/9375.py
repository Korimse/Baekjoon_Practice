T = int(input())

for _ in range(T):
    result = 1
    n = int(input())
    wear = {}
    for i in range(n):
        c, w = input().split()
        if w in wear:
            wear[w].append(c)
        else:
            wear[w] = [c]
    for w in wear:
        result *= len(wear[w])+1
    print(result-1)