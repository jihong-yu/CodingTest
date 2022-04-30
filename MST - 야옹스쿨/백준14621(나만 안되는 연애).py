import sys

input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union_(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    parent[a] = b


N, M = map(int, input().split())
school = [''] + list(input().split())
parent = [i for i in range(N + 1)]
info = []

for _ in range(M):
    u, v, d = map(int, input().split())
    info.append((u, v, d))

info.sort(key=lambda x: x[2])

ans = 0
cnt = 0
for i in info:
    a, b, d = i

    if find(a) != find(b) and school[a] != school[b]:
        union_(a, b)
        ans += d
        cnt += 1

if cnt != N - 1:
    print(-1)
else:
    print(ans)
