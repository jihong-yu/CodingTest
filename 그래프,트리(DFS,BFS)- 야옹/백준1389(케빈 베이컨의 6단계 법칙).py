from collections import deque

N, M = map(int, input().split())
graph = [set() for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

bacon = []  # 베이컨 수 저장


def bfs(v):
    global result
    visited[v] = True
    queue = deque([[v, 0]])

    while queue:

        start, count = queue.popleft()
        result += count
        for i in graph[start]:
            if not visited[i]:
                visited[i] = True
                queue.append([i, count + 1])


for i in range(1, N + 1):
    visited = [False] * (N + 1)
    result = 0
    bfs(i)
    bacon.append(result)

print(bacon.index(min(bacon)) + 1)
