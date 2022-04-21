import heapq
import sys

input = sys.stdin.readline
N, M, K, X = map(int, input().split())  # 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((1, b))

ans = []

distance = [1 << 30] * (N + 1)


def bfs(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, cur = heapq.heappop(q)

        if dist == K:
            ans.append(cur)
        elif dist > K:
            return

        if dist > distance[cur]:
            continue

        for nxt_cost, nxt in graph[cur]:
            if nxt_cost + dist < distance[nxt]:
                distance[nxt] = nxt_cost + dist
                heapq.heappush(q, (distance[nxt], nxt))


bfs(X)
if not ans:
    print(-1)
else:
    ans.sort()
    for i in ans:
        print(i)
