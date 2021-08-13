n = int(input())
idx = 0
answer = []
paper = list(map(int, input().split()))
balloon = [i for i in range(1,n+1)]

temp = paper.pop(idx)
answer.append(balloon.pop(idx))

while paper:
    if temp < 0:
        idx = (idx + temp) %len(paper)
    else:
        idx = (idx + (temp - 1)) % len(paper)
    temp = paper.pop(idx)
    answer.append(balloon.pop(idx))

for i in answer:
    print(i, end = ' ')