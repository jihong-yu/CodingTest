import sys

input = sys.stdin.readline

N, K = map(int, input().split())
mak = [int(input()) for _ in range(N)]

s = 1
e = max(mak)


def check(mid):

    total = 0
    for i in mak:
        total += (i // mid)

    return K <= total
ans = 0

while s <= e:

    mid = (s + e) // 2

    if check(mid):
        ans = mid
        s = mid + 1
    else:
        e = mid - 1

print(ans)