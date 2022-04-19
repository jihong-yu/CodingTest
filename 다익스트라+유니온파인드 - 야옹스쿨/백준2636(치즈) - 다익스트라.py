import heapq

N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]  # 상 우 하 좌
dc = [0, 1, 0, -1]  # 상 우 하 좌
distance = [[1e10] * M for _ in range(N)]
time_ = 0


def bfs():
    global time_

    q = []
    heapq.heappush(q, (cheese[0][0], 0, 0))
    distance[0][0] = cheese[0][0]
    while q:
        cost, r, c = heapq.heappop(q)
        time_ = cost  # 걸린시간을 저장(마지막에 저장된 값이 제일 마지막에 녹은 치즈의 시간)

        if cost > distance[r][c]:
            continue

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            # if cost + cheese[nr][nc] > 0 and not cheese[nr][nc]:
            #     heapq.heappush(q, (0, nr, nc))
            if cost + cheese[nr][nc] < distance[nr][nc]:
                distance[nr][nc] = cost + cheese[nr][nc]
                heapq.heappush(q, (distance[nr][nc], nr, nc))


bfs()
print(time_)

# 만약 1내부에 있는 0들도 같은 거리로 인식이 되기 때문에 해당 위치는 0으로 초기화 해주어야 한다.
for i in range(N):
    for j in range(M):
        if not cheese[i][j]:
            distance[i][j] = 0

count_ = 0  # 마지막에 남은 치즈 개수 체크
if time_ != 0:  # 만약 시간이 0아니라면(즉, 0은 체크하면 안됨)
    for i in distance:
        count_ += i.count(time_)
print(count_)
