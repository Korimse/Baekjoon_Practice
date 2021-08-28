import copy
T = int(input())

def solve(array, n):
  if len(array) == n:
    resultList.append(copy.deepcopy(array))
    return
  array.append(' ')
  solve(array, n)
  array.pop()

  array.append('+')
  solve(array, n)
  array.pop()

  array.append('-')
  solve(array, n)
  array.pop()

for _ in range(T):
  n = int(input())
  resultList = []
  solve([], n-1)

  integers = [i for i in range(1, n+1)]
  for result in resultList:
    string = ""
    for i in range(n-1):
      string += str(integers[i]) + result[i]
    string += str(integers[-1])
    if eval(string.replace(" ", "")) == 0:
      print(string)