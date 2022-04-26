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

    parent[a] = b


N = int(input())
parent = [i for i in range(N + 1)]

for _ in range(N - 2):
    a, b = map(int, input().split())
    union_(a, b)

for i in range(2, N + 1):

    if find(1) != find(i):
        print(1, i)
        break

