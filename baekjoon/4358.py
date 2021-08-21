import sys

input = sys.stdin.readline

trees = {}

n = 0
while True:
    tree = input().rstrip()
    if not tree:
        break
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1
    n+=1

ls = list(trees.keys())
ls.sort()
for tree in ls:
    print('%s %.4f' %(tree, trees[tree]/n*100))