import sys

input = sys.stdin.readline

K, N = map(int, input().split())
len = []
for _ in range(K):
    len.append(int(input()))

s = 1
e = max(len)


def check(mid):
    total = 0
    for i in len:
        total += (i // mid)

    return total >= N


ans = 0
while s <= e:

    mid = (s + e) // 2
    if check(mid):
        ans = mid
        s = mid + 1
    else:
        e = mid - 1

print(ans)
