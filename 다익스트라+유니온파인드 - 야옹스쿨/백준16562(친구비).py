import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)


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
    cost[b] = min(cost[a], cost[b])


N, M, K = map(int, input().split())

parent = [i for i in range(N + 1)]

arr = [0] + list(map(int, input().split()))
cost = arr[:]
for _ in range(M):
    a, b = map(int, input().split())
    union_(a, b)

ans = 0

for i in range(1, N + 1):
    if parent[i] == i:
        ans += cost[i]

if ans > K:
    print('Oh no')
else:
    print(ans)
