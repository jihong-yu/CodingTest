def dfs(depth, weight):
    global ans

    if weight > K:
        return -100000000

    if depth == N:
        return 0

    if dp[depth][weight] != -1:
        return dp[depth][weight]

    dp[depth][weight] = max(dfs(depth + 1, weight + bag[depth][0]) + bag[depth][1], dfs(depth + 1, weight))

    return dp[depth][weight]


N, K = map(int, input().split())

bag = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[-1] * (K + 1) for _ in range(N + 1)]
ans = 0

print(dfs(0, 0))
