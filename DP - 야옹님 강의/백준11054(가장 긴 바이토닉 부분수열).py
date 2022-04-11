N = int(input())
arr = list(map(int, input().split()))

reversed_arr = list(reversed(arr))

# def dfs(cur, pre, k):
#     if cur == k + 1:
#         return 0
#
#     if dp[cur][pre] != -1:
#         return dp[cur][pre]
#
#     if arr[cur] > arr[pre]:
#         dp[cur][pre] = max(dfs(cur + 1, cur, k) + 1, dfs(cur + 1, pre, k))
#     else:
#         dp[cur][pre] = dfs(cur + 1, pre, k)
#
#     return dp[cur][pre]
#
#
# def dfs_2(cur, pre, k):
#     if cur == k - 1:
#         return 0
#
#     if dp[cur][pre] != -1:
#         return dp[cur][pre]
#
#     if arr[cur] > arr[pre]:
#         dp[cur][pre] = max(dfs_2(cur - 1, cur, k) + 1, dfs_2(cur - 1, pre, k))
#     else:
#         dp[cur][pre] = dfs_2(cur - 1, pre, k)
#
#     return dp[cur][pre]


ans = 0
# for i in range(N):
#     dp = [[-1] * (N + 1) for _ in range(N + 1)]
#     ans = max(ans, dfs(0, -1, i) + dfs_2(N - 1, N, i))
dp_1 = [1] * N
dp_2 = [1] * N
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_1[i] = max(dp_1[i], dp_1[j] + 1)

for i in range(N)[::-1]:
    for j in range(i + 1, N)[::-1]:
        if arr[i] > arr[j]:
            dp_2[i] = max(dp_2[i], dp_2[j] + 1)

ans = 0
for i in range(N):
    ans = max(ans, dp_1[i] + dp_2[i])
print(ans - 1)
