import sys

input = sys.stdin.readline

N = int(input())

dp = [[0, 0, 0], [0, 0, 0]]
dp2 = [[1e6, 1e6, 1e6], [0, 0, 0]]
idx = 0

for i in range(1, N + 1):
    arr = list(map(int, input().split()))
    for j in range(3):
        dp2[idx][j] = 1e6
        for k in range(3):
            if abs(j - k) >= 2:
                continue

            dp[idx][j] = max(dp[idx][j], dp[not idx][k] + arr[j])
            dp2[idx][j] = min(dp2[idx][j], dp2[not idx][k] + arr[j])

    idx = not idx

print(max(dp[not idx]), min(dp2[not idx]))
