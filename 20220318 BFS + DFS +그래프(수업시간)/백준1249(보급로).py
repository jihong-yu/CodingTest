import heapq


def dijkstra(start_r, start_c):
    global ans

    q = []
    heapq.heappush(q, (start_r, start_c, 0))

    while q:
        r, c, cost = heapq.heappop(q)
        if r == N - 1 and c == N - 1:
            if ans > cost:
                ans = cost
            return
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and cost <= dist[nr][nc]:
                nxt_cost = war[nr][nc] + cost
                if nxt_cost < dist[nr][nc]:
                    dist[nr][nc] = nxt_cost
                    heapq.heappush(q, (nr, nc, nxt_cost))


dr = [-1, 1, 0, 0]  # 상 하 좌 우
dc = [0, 0, -1, 1]  # 상 하 좌 우
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    war = [list(map(int, input())) for _ in range(N)]
    INF = 1e10
    dist = [[INF] * N for _ in range(N)]
    ans = INF
    dijkstra(0, 0)
    print(f'#{tc} {ans}')
