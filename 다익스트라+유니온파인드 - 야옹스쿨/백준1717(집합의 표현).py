import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union_(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    if rank[a] > rank[b]:
        parent[b] = a
    elif rank[a] < rank[b]:
        parent[a] = b
    else:
        parent[a] = b
        rank[b] += 1


N, M = map(int, input().split())

parent = [i for i in range(N + 1)]
rank = [0 for _ in range(N + 1)]
for _ in range(M):
    oper, a, b = map(int, input().split())

    if oper:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        union_(a, b)
