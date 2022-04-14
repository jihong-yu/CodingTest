from collections import deque

N, M = map(int, input().split())
maze = [input() for _ in range(N)]
dr = [-1, 0, 1, 0]  # 상 우 하 좌
dc = [0, 1, 0, -1]  # 상 우 하 좌
st_r, st_c = 0, 0
for i in range(N):
    for j in range(M):
        if maze[i][j] == '0':
            st_r = i
            st_c = j

visited = [[[False] * (1 << 6) for _ in range(M)] for _ in range(N)]

queue = deque([(st_r, st_c, 0, 0)])
visited[st_r][st_c][0] = True
while queue:
    r, c, dis, key = queue.popleft()

    if maze[r][c] == '1':
        print(dis)
        exit()

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= M or maze[nr][nc] == '#' or visited[nr][nc][key]:
            continue

        nkey = key
        if 'A' <= maze[nr][nc] <= 'F':
            if not (nkey & (1 << ord(maze[nr][nc]) - ord('A'))):  # 해당 비트가 켜져있는지 확인
                continue

        elif 'a' <= maze[nr][nc] <= 'f':
            nkey |= (1 << ord(maze[nr][nc]) - ord('a'))  # 해당비트를 킨다

        visited[nr][nc][nkey] = True
        queue.append((nr, nc, dis + 1, nkey))

print(-1)
