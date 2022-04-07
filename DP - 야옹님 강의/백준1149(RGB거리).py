import sys

sys.setrecursionlimit(50000)

N = int(input())
homes = [list(map(int, input().split())) for _ in range(N)]
ans = 1 << 60
arr = [-1] * N

dp = [-1] * N
temp = 0
for i in range(N)[::-1]:
    temp += min(homes[i])
    dp[i] = temp


def recur(cur, pre, total):
    global ans

    if cur == N:
        if total < ans:
            ans = total
        return

    if total + dp[cur] >= ans:
        return

    for i in range(3):
        arr[cur] = i
        if arr[pre] != arr[cur]:
            recur(cur + 1, cur, total + homes[cur][i])
        arr[cur] = -1


recur(0, -1, 0)
print(ans)
