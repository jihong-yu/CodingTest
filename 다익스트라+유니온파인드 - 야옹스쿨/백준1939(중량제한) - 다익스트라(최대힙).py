import heapq
import sys

input = sys.stdin.readline


def dijkstra(v1, v2):
    global ans
    q = []
    heapq.heappush(q, (-(1 << 60), v1))

    while q:

        cost, cur = heapq.heappop(q)
        cost = (-cost)

        if cur == v2:
            print(cost)
            return
        # 만약 현재 비용이 구한 비용보다 적다면 실행x
        if cost < distance[cur]:
            continue

        for nxt, nxt_cost in graph[cur]:
            # 만약 다음노드에 저장된 중량값이 현재까지 구한 cost와 다음 노드의 중량보다 작다면
            if distance[nxt] < nxt_cost and distance[nxt] < cost:
                distance[nxt] = min(cost, nxt_cost)  # 그중 작은값을 최대 중량으로 저장 후
                heapq.heappush(q, (-distance[nxt], nxt))  # 최대 값으로 힙에 넣어준다


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

v1, v2 = map(int, input().split())
distance = [0] * (N + 1)
dijkstra(v1, v2)
