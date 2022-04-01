import sys

input = sys.stdin.readline

N = int(input())
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 2)


#dp[cur] = max(dfs_2(cur + arr[cur][0]) + arr[cur][1], dfs_2(cur + 1))

for i in range(1, N + 1):
    if arr[i][0] <= (N + 1) - i:
        dp[i + arr[i][0]] = max(dp[i + arr[i][0]], dp[i] + arr[i][1])

    dp[i + 1] = max(dp[i + 1], dp[i])

print(dp[-1])