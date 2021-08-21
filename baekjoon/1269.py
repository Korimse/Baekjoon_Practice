n, m = map(int, input().split())

arrA = set(map(int, input().split()))
arrB = set(map(int, input().split()))
print(len(arrA-arrB) + len(arrB-arrA))
