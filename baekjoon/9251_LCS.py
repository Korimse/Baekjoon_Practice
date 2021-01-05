n = input()
m = input()
result = [[0 for _ in range(len(n)+1)]for _ in range(len(m)+1)]

for i in range(1, len(m)+1):
    for j in range(1, len(n)+1):
        if n[j-1] == m[i-1]:
            result[i][j] = result[i-1][j-1]+1
        else:
            result[i][j] = max(result[i-1][j], result[i][j-1])

print(result[len(m)][len(n)])