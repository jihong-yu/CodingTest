import heapq
import sys

input = sys.stdin.readline


def dijkstra():
    q = []
    heapq.heappush(q, (arr[0][0], 0, 0))
    distance[0][0] = arr[0][0]
    while q:
        cost, r, c = heapq.heappop(q)

        if r == N - 1 and c == N - 1:
            return cost

        if cost > distance[r][c]:
            continue

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            if cost + arr[nr][nc] < distance[nr][nc]:
                distance[nr][nc] = cost + arr[nr][nc]
                heapq.heappush(q, (distance[nr][nc], nr, nc))


dr = [-1, 0, 1, 0]  # 상 우 하 좌
dc = [0, 1, 0, -1]  # 상 우 하 좌
tc = 0
while True:
    tc += 1
    N = int(input())
    if N == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(N)]
    INF = 1 << 20
    distance = [[INF] * N for _ in range(N)]
    print(f'Problem {tc}: {dijkstra()}')
