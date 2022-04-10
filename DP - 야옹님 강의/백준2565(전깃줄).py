N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x: (x[0]))
arr += [[0, 0]]
dp = [[-1] * (N + 1) for _ in range(N + 1)]


def dfs(cur, pre):
    if cur >= N:
        return 0

    if dp[cur][pre] != -1:
        return dp[cur][pre]

    if arr[cur][1] > arr[pre][1]:
        dp[cur][pre] = max(dfs(cur + 1, cur) + 1, dfs(cur + 1, pre))
    else:
        dp[cur][pre] = dfs(cur + 1, pre)

    return dp[cur][pre]


print(N - dfs(0, -1))
