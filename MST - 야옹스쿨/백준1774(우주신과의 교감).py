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
parent = [i for i in range(N + 1)]
gods = []

for i in range(N):
    x, y = map(int, input().split())
    gods.append((i + 1, x, y))

for j in range(M):
    a, b = map(int, input().split())
    union_(a, b)

distance = []
for i in range(N):
    for j in range(i + 1, N):
        a, b = gods[i][0], gods[j][0]
        d = ((gods[i][1] - gods[j][1]) ** 2 + (gods[i][2] - gods[j][2]) ** 2) ** 0.5
        distance.append((a, b, d))

distance.sort(key=lambda x: x[2])

ans = 0
for i in distance:
    a, b, d = i

    if find(a) != find(b):
        union_(a, b)
        ans += d

print(f'{ans:.2f}')
