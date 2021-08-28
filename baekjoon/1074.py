N, r, c = map(int, input().split())

def solve(N, x, y):
    global result

    if N == 2:
        if x == r and y == c:
            print(result)
            return
        result += 1
        if x == r and y + 1 == c:
            print(result)
            return
        result += 1
        if x +1 == r and y == c:
            print(result)
            return
        result += 1
        if x + 1 == r and y + 1 == c:
            print(result)
            return
        result += 1
        return
    solve(N / 2, x, y)
    solve(N / 2, x, y + N / 2)
    solve(N / 2, x + N / 2, y)
    solve(N / 2, x + N / 2, y + N / 2)

result = 0
solve(2**N, 0, 0)