import sys
sys.setrecursionlimit(10000)

def recur(cur, prv):
    ret = 0xffffff
    if cur > N:
        return ret

    if cur == N:
        return 0

    if memo[cur][prv] != -1:
        return memo[cur][prv]

    for i in range(3):
        if prv == i:
            continue
        ret = min(ret, recur(cur + 1, i) + mat[cur][i])
        memo[cur][prv] = ret
    return ret

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
memo = [[-1] * (N+10) for _ in range(N+10)]

print(recur(0, -10))