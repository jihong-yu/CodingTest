import sys

sys.setrecursionlimit(100000)
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


V, E = map(int, input().split())

parent = [i for i in range(V + 1)]

graph = []
for _ in range(E):
    a, b, cost = map(int, input().split())
    graph.append((a, b, cost))

graph.sort(key=lambda x: x[2])
ans = 0
for i in graph:

    if find(i[0]) != find(i[1]):
        union_(i[0], i[1])
        ans += i[2]

print(ans)
