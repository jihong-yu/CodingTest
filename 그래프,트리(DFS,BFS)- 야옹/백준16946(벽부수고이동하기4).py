from collections import deque


def bfs(start_r, start_c):
    visited = [[False] * M for _ in range(N)]
    queue = deque([[start_r, start_c]])
    cnt = 1
    visited[start_r][start_c] = True
    while queue:
        r, c = queue.popleft()
        if arr[r][c] == 0:
            cnt += 1

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M or arr[nr][nc] >= 1 or visited[nr][nc]:
                continue
            visited[nr][nc] = True
            queue.append([nr, nc])

    arr[start_r][start_c] = cnt


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
dr = [-1, 0, 1, 0]  # 상 우 하 좌
dc = [0, 1, 0, -1]  # 상 우 하 좌
loc = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            bfs(i, j)

for i in range(N):
    for j in range(M):
        print(arr[i][j], end="")
    print()
