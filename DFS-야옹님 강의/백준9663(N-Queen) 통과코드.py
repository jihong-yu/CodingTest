def checking(r, c):
    for j in range(len(check)):
        if abs(j - r) == abs(check[j] - c):
            return False
    return True


def dfs(r):
    global count

    if r == N:
        count += 1
        return

    for col in range(N):
        if col not in check:
            if checking(r, col):
                check.append(col)
                dfs(r + 1)
                check.pop()


N = int(input())

check = []
count = 0


dfs(0)
print(count)