import sys

input = sys.stdin.readline

N = int(input())
array = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

dp = [[[0] * 11 for _ in range(N + 1)] for _ in range(N + 1)]


for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, 11):
            if k == array[i][j]:
                dp[i][j][k] += 1
            dp[i][j][k] += dp[i-1][j][k] + dp[i][j-1][k] - dp[i-1][j-1][k]


Q = int(input())
for _ in range(Q):
    x1, y1, x2, y2 = map(int, input().split())
    sum_ = 0
    for k in range(1, 11):
        if dp[x2][y2][k] - dp[x2][y1 - 1][k] - dp[x1-1][y2][k] + dp[x1-1][y1-1][k]:
            sum_ += 1
    print(sum_)