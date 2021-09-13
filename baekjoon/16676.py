goal = input()
words = '1'*len(goal)

if len(goal) == 1:
    print(1)
elif int(goal) >= int(words):
    print(len(goal))
else:
    print(len(goal)-1)

