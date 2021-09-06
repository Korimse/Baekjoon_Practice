alp = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]
n, m = map(int, input().split())

a, b = map(str, input().split())
string = ''
if n < m:
    for i in range(n):
        string += a[i]+b[i]
    string += b[n:m]
else:
    for i in range(m):
        string += a[i]+b[i]
    string += a[m:n]
lst = [alp[ord(i)-ord('A')] for i in string]
for i in range(n+m-2):
    for j in range(n+m-i-1):
        lst[j] += lst[j+1]
print("{}%".format(lst[0] %10*10 + lst[1] %10))
