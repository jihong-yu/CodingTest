from collections import deque


def bfs(v):
    global ans, result

    visited[v] = True
    queue = deque([v])
    count = 0

    while queue:

        node = queue.popleft()
        count += 1

        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

    if count > ans:
        result = [v]
        ans = count
    elif count == ans:
        result.append(v)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

ans = 0
result = []
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    bfs(i)

result.sort()
print(*result)
