import heapq
import sys

input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
for i in range(E):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
INF = 1e10
distance = [INF] * (V + 1)


def dijkstra(s):
    q = []
    distance[s] = 0
    heapq.heappush(q, (0, s))

    while q:
        cost, cur = heapq.heappop(q)

        if cost > distance[cur]:
            continue

        for nxt, nxt_cost in graph[cur]:
            if nxt_cost + cost < distance[nxt]:
                distance[nxt] = nxt_cost + cost
                heapq.heappush(q, (distance[nxt], nxt))


dijkstra(K)
for i in range(1, len(distance)):
    if distance[i] != INF:
        print(distance[i])
    else:
        print('INF')
