def checking(r, c):
    for j in range(r):
        if check[j] == c or abs(j - r) == abs(check[j] - c):
            return False
    return True


def dfs(r):
    global count

    if r == N:
        count += 1
        return

    for col in range(N):
        if checking(r, col):
            check[r] = col
            dfs(r + 1)


N = int(input())

check = [0] * N
count = 0


dfs(0)
print(count)



