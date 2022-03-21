from collections import deque

N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]
# 방문처리를 두가지로 나누어서 해준다. visited[r][c][0] => 벽을 깨지않고 이동하는 방문처리
# visited[r][c][1] => 벽을 깨고 이동하는 방문처리
visited = [[[False, False] for _ in range(M)] for _ in range(N)]

dr = [-1, 0, 1, 0]  # 행 상 우 하 좌
dc = [0, 1, 0, -1]  # 열 상 우 하 좌

min_ = 1 << 60


def bfs(r, c):
    global min_

    queue = deque([[r, c, 0, 0]])  # [행,열,거리,벽을 깬 횟수]를 큐에 저장
    visited[r][c][0] = True  # 우선 첫번째 장소 방문처리 (문제에 조건에 따라 항상 0)

    while queue:
        r, c, distance, count = queue.popleft()
        if r == N - 1 and c == M - 1:
            if distance < min_:
                min_ = distance

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 큐에서 꺼낸 값을 따로 변수에 저장하지 않고 변경할 경우
            # 해당 큐에서 진행하는 모든 방향의 변수에 영향을 준다.
            # 즉, count를 직접 변경해버리면 나머지 하,좌,우 방향에 count 값이 변경된채 계산이 된다.
            temp_count = count

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            # 만약 벽을 깬 횟수가 이미 1이고 다음도 벽이라면 혹은 이미 방문했다면
            if (temp_count == 1 and miro[nr][nc] == 1) or visited[nr][nc][temp_count]:
                continue

            if miro[nr][nc] == 1:
                # 0 -> 1로 갈때는 visited[nr][nc][0] , visited[nr][nc][1] 모두 방문처리해준다.
                visited[nr][nc][temp_count] = True
                temp_count += 1

            visited[nr][nc][temp_count] = True  # 다음 count에 따라 일반적인 방문처리
            queue.append([nr, nc, distance + 1, temp_count])


bfs(0, 0)
if min_ == 1 << 60:
    print(-1)
else:
    print(min_ + 1)
