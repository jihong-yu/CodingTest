import heapq
import sys


def dijkstra(s, des, distance):
    q = []
    distance[s] = 0
    heapq.heappush(q, (0, s))

    while q:
        cost, cur = heapq.heappop(q)

        if cur == des:
            return cost

        if cost > distance[cur]:
            continue

        for nxt, nxt_cost in graph[cur]:
            if nxt_cost + cost < distance[nxt]:
                distance[nxt] = nxt_cost + cost
                heapq.heappush(q, (distance[nxt], nxt))

    return INF


input = sys.stdin.readline
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(E):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))

v1, v2 = map(int, input().split())
dest_1 = [1, v1, v2, N]  # 경로1
dest_2 = [1, v2, v1, N]  # 경로2
INF = 1e10  # 무한대 값 설정

temp_dist_1 = 0  # 1 -> v1 -> v2 -> N 까지의 경로의 길이
temp_dist_2 = 0  # 1 -> v2 -> v1 -> N 까지의 경로의 길이
for i in range(3):
    distance = [INF] * (N + 1)
    temp_dist_1 += dijkstra(dest_1[i], dest_1[i + 1], distance)
    distance2 = [INF] * (N + 1)
    temp_dist_2 += dijkstra(dest_2[i], dest_2[i + 1], distance2)

ans = min(temp_dist_1, temp_dist_2)  # 둘중 최단경로를 저장
if ans >= INF:  # 해당 최단경로가 무한대를 넘는다면
    print(-1)
else:  # 그 외의 경우
    print(ans)
