from collections import deque
T = int(input())

for i in range(T):
    arr = input()
    n = int(input())
    data = input()[1:-1].split(",")
    if data[0] != '':
        data = deque(data)
    else:
        data = deque()

    isTrue = True
    directFlag = True
    count = 0
    for i in range(len(arr)):
        if arr[i] == 'R':
            if directFlag == True:
                directFlag = False
            elif directFlag == False:
                directFlag = True
            count+=1
        elif arr[i] == 'D':
            if len(data) == 0:
                print("error")
                isTrue = False
                break
            
            if directFlag == True:
                data.popleft()
            elif directFlag==False:
                data.pop()

    if count%2 != 0:
        data.reverse()

    if isTrue == True:
        print("[", end='')
        for i in range(len(data)):
            print(data[i], end="")
            if i != len(data)-1:
                print(",", end="")
        print("]")
