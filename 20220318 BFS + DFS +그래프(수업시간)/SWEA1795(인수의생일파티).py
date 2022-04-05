import heapq


def dijkstra(v, graph):
    q = []
    heapq.heappush(q, (0, v))
    INF = 1 << 30
    dist = [INF] * (N + 1)
    dist[v] = 0
    while q:

        cost, cur = heapq.heappop(q)

        if cost > dist[cur]:
            continue

        for i in graph[cur]:
            nxt, nxt_cost = i[0], i[1] + cost
            if nxt_cost < dist[nxt]:
                dist[nxt] = nxt_cost
                heapq.heappush(q, (nxt_cost, nxt))

    return dist


T = int(input())

for tc in range(1, T + 1):
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    graph_reverse = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        graph[x].append((y, c))  # x -> y 까지의 거리 저장
        graph_reverse[y].append((x, c))  # y -> x까지의 거리 저장(뒤집어서 저장)

    dist1 = dijkstra(X, graph)  # 파티장(X)에서 집으로 돌아오는 거리 계산
    dist2 = dijkstra(X, graph_reverse)  # 각각의 번호에서 파티장(X)까지 거리 계산

    ans = 0
    for i in range(1, N + 1):  # 각각의 지점에서 거리 구하기
        if dist1[i] + dist2[i] > ans:
            ans = dist1[i] + dist2[i]
    print(f'#{tc} {ans}')
