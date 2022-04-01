import sys

input = sys.stdin.readline
sys.setrecursionlimit(800000)

N = int(input())
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
dp = {}


def dfs_2(cur):
    if cur > N + 1:
        return -10000000
    elif cur == N + 1:
        return 0

    if dp.get(cur, -1) != -1:
        return dp[cur]

    dp[cur] = max(dfs_2(cur + arr[cur][0]) + arr[cur][1], dfs_2(cur + 1))

    return dp[cur]


print(dfs_2(1))
