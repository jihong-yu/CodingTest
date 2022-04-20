import heapq
import sys

input = sys.stdin.readline


def dijkstra(s, graph: list, distance: list):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0
    while q:
        cost, cur = heapq.heappop(q)

        if distance[cur] < cost:
            continue

        for nxt, nxt_cost in graph[cur]:
            if distance[nxt] > nxt_cost + cost:
                distance[nxt] = nxt_cost + cost
                heapq.heappush(q, (distance[nxt], nxt))


N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
graph_r = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph_r[b].append((a, cost))

distance_r = [1e10] * (N + 1)
dijkstra(X, graph_r, distance_r)

distance = [1e10] * (N + 1)
dijkstra(X, graph, distance)

ans = 0
for i in range(1, N + 1):
    ans = max(ans, distance[i] + distance_r[i])

print(ans)
