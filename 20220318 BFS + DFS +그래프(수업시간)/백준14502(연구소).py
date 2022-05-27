from collections import deque

N, M = map(int, input().split())
map_ = [list(map(int, input().split())) for _ in range(N)]

brr = []
zero = []
two = []
max_ = 0

dr = [-1, 0, 1, 0]  # 행 상 우 하 좌
dc = [0, 1, 0, -1]  # 열 상 우 하 좌
for i in range(N):
    for j in range(M):
        if not map_[i][j]:
            zero.append((i, j))
        elif map_[i][j] == 2:
            two.append((i, j))


def bfs(dump_map: []):
    global max_

    visited = [[False] * M for _ in range(N)]
    queue = deque([])
    for i in range(len(two)):
        queue.append(two[i])

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc] or dump_map[nr][nc]:
                continue

            dump_map[nr][nc] = 2
            visited[nr][nc] = True
            queue.append((nr, nc))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if not dump_map[i][j]:
                cnt += 1

    if max_ < cnt:
        max_ = cnt


def dfs(cur, start):
    if cur == 3:
        dump_map = []
        for i in range(N):
            dump_map.append(map_[i][:])

        for r, c in brr:
            dump_map[r][c] = 1

        bfs(dump_map)
        return

    for i in range(start, len(zero)):
        brr.append(zero[i])
        dfs(cur + 1, i + 1)
        brr.pop()


dfs(0, 0)
print(max_)
