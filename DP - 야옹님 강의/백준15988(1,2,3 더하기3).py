import sys

input = sys.stdin.readline


def recur(total):
    ret = 0
    print(total)
    if total > N:
        return 0

    if total == N:
        return 1

    if dp.get(total, -1) != -1:
        return dp[total]

    for i in range(1, 3 + 1):
        ret = recur(total + i)

    dp[total] = ret

    return dp[total]


dp = {}

dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, 1000001):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N])
