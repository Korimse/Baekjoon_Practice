s = "xababcdcdababcdcd"
answer = 
for i in range(1, len(s)):
  count = 1
  ans = ''
  for j in range(0, len(s), i):
    if s[j:j+i] == s[j+i:j+(2*i)]:
      count += 1
    else:
      if count == 1:
        ans += s[j:j+i]
      else:
        ans += str(count) + s[j:j+i]
      count = 1
  answer = min(answer, len(ans))
print(answer)