import sys
from collections import deque

sys.setrecursionlimit(5000)
input = sys.stdin.readline

def dfs(cur):
    visited[cur] = True

    for nxt in graph[cur]:
        if not visited[nxt]:
            parent[nxt] = cur
            dfs(nxt)


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                parent[i] = v
                queue.append(i)


N = int(input())  # 간선의 개수는 노드개수 - 1
graph = [[] for _ in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
parent = [0] * (N + 1)

bfs(1)

for i in parent[2:]:
    print(i)
