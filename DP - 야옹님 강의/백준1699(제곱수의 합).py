import sys

sys.setrecursionlimit(100000)
N = int(input())

dp = [10000000] * (N + 1)


def recur(total):
    ret = 100000000
    if total > N:
        return 100000000
    elif total == N:
        return 0

    if dp[total] != -1:
        return dp[total]

    for i in range(1, N + 1):
        ret = min(ret, recur(total + i * i) + 1)

    dp[total] = ret

    return dp[total]


# print(recur(0))
dp[0] = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i < j * j:
            break

        dp[i] = min(dp[i], dp[i - j * j] + 1)

print(dp[N])
