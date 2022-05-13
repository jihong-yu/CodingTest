import sys

input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union_(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    parent[a] = b


N = int(input())
P = int(input())
g = [int(input()) for _ in range(P)]

parent = [x for x in range(N + 1)]
ans = 0

for i in g:

    x = find(i)
    if x == 0:
        break

    union_(x, x - 1)
    ans += 1

print(ans)
