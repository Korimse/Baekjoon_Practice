answer = []
people = 0

while True:
    a,b = map(int, input().split())

    if b == 0:
        break
    
    people -= a
    people += b
    answer.append(people)

print(answer)