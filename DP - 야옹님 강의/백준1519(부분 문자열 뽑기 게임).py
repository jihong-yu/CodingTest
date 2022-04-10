import sys

sys.setrecursionlimit(100000)
N = input()

dp = [-1 for _ in range(int(N) + 1)]
ans = 1e10


def dfs(num, turn, cur):
    global ans

    if len(num) == 1:
        dp[int(num)] = 0
        return dp[int(num)]

    if dp[int(num)] != -1:
        return dp[int(num)]

    for i in range(len(num)):
        for j in range(i, len(num)):
            temp = num[i:j + 1]
            if len(temp) == len(num) or temp == '0':
                continue
            if cur and not dfs(str(int(num) - int(temp)), not turn, cur + 1):
                dp[int(num)] = 1
                return dp[int(num)]
            elif not cur:
                if not dfs(str(int(num) - int(temp)), not turn, cur + 1):
                    dp[int(num)] = 1
                    if cur == 0 and ans > int(temp):
                        ans = int(temp)

    if dp[int(num)] == -1:
        dp[int(num)] = 0
    return dp[int(num)]


score = dfs(N, 1, 0)
if score:
    score = ans
else:
    score = -1
print(score)
