import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def recur(total):
    ret = 0

    if total > N:
        return 0

    if total == N:
        return 1

    if dp[total] != -1:
        return dp[total] % 1000000009

    for i in range(1, 3 + 1):
        ret += recur(total + i)

    dp[total] = ret % 1000000009

    return dp[total] % 1000000009


T = int(input())
for _ in range(T):
    N = int(input())
    dp = [-1] * (N + 1)
    print(recur(0))
