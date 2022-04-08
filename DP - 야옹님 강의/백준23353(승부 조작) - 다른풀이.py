import sys

sys.setrecursionlimit(5000)


def dfs(r, c, check, dir):
    ret = 0

    if r < 0 or c >= N or r >= N or c < 0 or board[r][c] == 0:
        return 0

    if dp[r][c][dir][check] != -1:
        return dp[r][c][dir][check]

    if check and board[r][c] == 2:
        return 0

    if not check and board[r][c] == 2:
        check = 1

    nr = r + dr[dir]
    nc = c + dc[dir]

    dp[r][c][dir][check] = max(dfs(nr, nc, check, dir) + 1, ret)

    return dp[r][c][dir][check]


dr = [0, 1, 1, 1]  # 우 우하 하 좌하
dc = [1, 1, 0, -1]  # 우 우하 하 좌하
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[[-1, -1] for _ in range(4)] for _ in range(N)] for _ in range(N)]

ans = 0

for r in range(N):
    for c in range(N):
        for i in range(4):
            ans = max(ans, dfs(r, c, 0, i))

print(ans)
