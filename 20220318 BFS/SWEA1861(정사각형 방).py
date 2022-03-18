from collections import deque

T = int(input())
dr = [-1, 0, 1, 0]  # 상 우 하 좌
dc = [0, 1, 0, -1]  # 상 우 하 좌


def bfs(r, c):
    global max_
    global start

    queue = deque([[r, c, array[r][c]]])

    while queue:
        r, c, temp_start = queue.popleft()
        # 만약 방문값이 같거나 크다면
        if visited[r][c] >= max_:
            if visited[r][c] == max_:  # 같다면
                if start > temp_start:  # 작을때만 시작값 변경
                    start = temp_start
            else:  # 크다면
                max_ = visited[r][c]  # 최대 값 변경
                start = temp_start  # 시작값 변경

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr >= N or nr < 0 or nc >= N or nc < 0 or visited[nr][nc] != 1 or array[nr][nc] != (array[r][c] + 1):
                continue

            visited[nr][nc] = visited[r][c] + 1
            queue.append([nr, nc, temp_start])


for tc in range(1, T + 1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]

    max_ = 1  # 이동 횟수 저장
    start = 1 << 60  # 시작 방번호 저장

    # 정방향으로 한번 실행(우,하 방향 검색)
    visited = [[1] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                bfs(i, j)

    # 역방향으로 한번 실행(좌,상 방향 검색)
    visited = [[1] * N for _ in range(N)]
    for i in range(N)[::-1]:
        for j in range(N)[::-1]:
            if visited[i][j] == 1:
                bfs(i, j)

    print(f'#{tc} {start} {max_}')
