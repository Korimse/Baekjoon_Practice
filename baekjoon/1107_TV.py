channel = int(input())
n = int(input())
if n == 0:
  disable = []
else:
  disable = list(map(int, input().split()))
result = abs(n-100)

for i in range(1000001):
  isTrue = True
  for j in str(i):
    if j in disable:
      isTrue = False
      break
  
  if isTrue == True:
    result = min(result, abs(channel-i)+len(str(i)))
print(result)