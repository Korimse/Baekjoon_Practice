n, l, k = map(int, input().split())

hard = 0
easy = 0
for i in range(n):
    a, b = map(int, input().split())

    if b <= l:
        hard += 1
    elif a <= l:
        easy += 1

answer = min(hard, k)*140
if hard < k:
    answer += min(k-hard, easy)*100
print(answer)