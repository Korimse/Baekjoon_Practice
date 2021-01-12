import copy

n = int(input())

def pro(array, n):
  if len(array) == n:
    arr.append(copy.deepcopy(array))
    return
  
  array.append(" ")
  pro(array, n)
  array.pop()

  array.append("+")
  pro(array, n)
  array.pop()

  array.append("-")
  pro(array, n)
  array.pop()

    

for _ in range(n):
  m = int(input())
  arr = []
  pro([], m-1)

  integers = [i for i in range(1, m+1)]
  for i in arr:
    s = ""
    for j in range(m-1):
      s += str(integers[j]) + i[j]
    s += str(integers[-1])
  
    if eval(s.replace(" ", "")) == 0:
      print(s)
  print()