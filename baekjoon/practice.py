import copy

info = [0,0,0,0,0,0,0,0,3,4,3]
n = 10
result = []
def lions(info, lion, n):
    global result
    # if lion[0:8] == [1,1,1,1,1,1,1,1]:
    #     result.append(copy.deepcopy(lion[8:11]))

    if sum(lion) >= n:
        if sum(lion) == n:
            print(lion)
        return 0
    
    
    for i in range(11):
        if lion[i] == 0:
            lion[i] = info[i] + 1
            lions(info, lion, n)
            lion[i] = 0
    
    for j in range(11):
        if lion[j] == 0:
            lion[j] = n - sum(lion)
            lions(info, lion, n)
            lion[j] = 0


lion = [0 for _ in range(11)]

lions(info, lion, n)
print(result)