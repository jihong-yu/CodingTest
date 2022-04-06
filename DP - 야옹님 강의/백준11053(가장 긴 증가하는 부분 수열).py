import sys

sys.setrecursionlimit(100000)

N = int(input())
A = list(map(int, input().split())) + [0]

dp = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]


def dfs(cur, pre):
    if cur == N:
        return 0

    if dp[cur][pre] != - 1:
        return dp[cur][pre]

    if A[cur] > A[pre]:
        ret = max(dfs(cur + 1, cur) + 1, dfs(cur + 1, pre))
    else:
        ret = dfs(cur + 1, pre)

    dp[cur][pre] = ret

    return dp[cur][pre]


#print(dfs(0, -1))

dp = [1 for i in range(N)]
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))