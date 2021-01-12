n = int(input())
arr = []
for i in range(n):
  arr.append(input())

alpha = [0]*26
for i in arr:
  k = 0
  while i:
    now = i[-1]
    alpha[ord(now) - ord('A')] += pow(10, k)
    k += 1
    i = i[:-1]

alpha.sort(reverse=True)

answer= 0
for i in range(9, 0, -1):
  answer += i*alpha[9-i]
print(answer)