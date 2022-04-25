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

    if rank[a] > rank[b]:
        parent[b] = a
        size[a] += size[b]
    elif rank[b] < rank[a]:
        parent[a] = b
        size[b] += size[a]
    else:
        parent[a] = b
        rank[b] += 1
        size[b] += size[a]


N = int(input())
parent = [i for i in range(1000000 + 1)]
rank = [0 for _ in range(1000000 + 1)]
size = [1 for _ in range(1000000 + 1)]
for _ in range(N):

    test = list(input().split())

    if len(test) >= 3:
        a, b = int(test[1]), int(test[2])
    else:
        c = int(test[1])

    oper = test[0]

    if oper == 'I':
        union_(a, b)
    else:
        print(size[find(c)])
