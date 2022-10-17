import sys

sys.setrecursionlimit(20000)
input = sys.stdin.readline

T = int(input())


def find_parent(node, find):
    if node:
        find.append(node)

        find_parent(parent[node], find)


for _ in range(T):

    N = int(input())

    parent = [0 for _ in range(N + 1)]
    for i in range(N - 1):
        parent_node, child = map(int, input().split())
        parent[child] = parent_node

    n1, n2 = map(int, input().split())

    find1 = []
    find_parent(n1, find1)
    find2 = []
    find_parent(n2, find2)

    answer = 0
    for i in range(-1, -min(len(find1), len(find2)) - 1, -1):
        if find1[i] != find2[i]:
            break
        answer = find1[i]

    print(answer)
