N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

dp = [[[1 << 30] * 3 for _ in range(3)] for _ in range(N)]


def recur(row, col, first_col):
    if row == N + 1:
        if col == first_col:
            return 1 << 30
        return 0

    if dp[row][col][first_col] != 1 << 30:
        return dp[row][col][first_col]

    for j in range(3):
        if row >= 1 and j == col:
            continue
        if row == 1:
            first_col = col
            dp[row][col][first_col] = min(dp[row][col][first_col], recur(row + 1, j, first_col) + house[row][col])
            return dp[row][col][first_col]
        else:
            dp[row][col][first_col] = min(dp[row][col][first_col], recur(row + 1, j, first_col) + house[row][col])

    return dp[row][col][first_col]


ans = 1 << 30
for i in range(N):
    start = i
    ans = min(ans, recur(0, i, i))

print(recur(0, 0, 0))
