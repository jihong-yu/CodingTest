import heapq
import sys

sys.setrecursionlimit(10000)

def dikstra(start):
    q = []
    heapq.heappush(q, (start, 0))

    while q:

        v, cost = heapq.heappop(q)

        if cost > dist[v]:
            continue

        for i in graph[v]:
            nxt, nxt_cost = i[0], i[1]
            if nxt_cost + cost < dist[nxt]:
                dist[nxt] = nxt_cost + cost
                heapq.heappush(q, (nxt, nxt_cost + cost))


T = int(input())

for tc in range(1, T + 1):

    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, c = map(int, input().split())
        graph[s].append((e, c))
    INF = 1e10
    dist = [INF] * (N + 1)
    dikstra(0)
    print(f'#{tc} {dist[-1]}')
