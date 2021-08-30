n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

isTrue = True
if max(crane) < max(box):
    print(-1)
else:
    crane.sort(reverse=True)
    box.sort(reverse=True)

    check = [False] * m
    position = [0] * n
    result = 0
    count = 0
    while True:
        if count == len(box):
            break
        for i in range(n):
            while position[i] < len(box):
                if not check[position[i]] and crane[i] >= box[position[i]]:
                    check[position[i]] = True
                    position[i] += 1
                    count += 1
                    break
                position[i] += 1
        print(position)
        result += 1
    print(box)
    print(result)