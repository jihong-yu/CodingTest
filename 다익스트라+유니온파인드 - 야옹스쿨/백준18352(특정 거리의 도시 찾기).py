import sys
from collections import deque

input = sys.stdin.readline
N, M, K, X = map(int, input().split())  # 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

ans = []

visited = [False] * (N + 1)


def bfs(start):
    queue = deque([[start, 0]])
    visited[start] = True
    while queue:
        cur, dist = queue.popleft()

        if dist == K:
            ans.append(cur)
        elif dist > K:
            return
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append([nxt, dist + 1])


bfs(X)
if not ans:
    print(-1)
else:
    ans.sort()
    for i in ans:
        print(i)
