import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
s = 0
e = max(trees)
ans = 0


def check(mid):
    total = 0
    for i in trees:
        total += max(0, i - mid)

    return total >= M


while s <= e:

    mid = (s + e) // 2
    if check(mid):
        ans = mid
        s = mid + 1
    else:
        e = mid - 1

print(ans)
