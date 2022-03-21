import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
bomool = []
land = []
for i in range(N):
    temp = list(map(str, input()))
    for j in range(len(temp)):
        if temp[j] == 'L':
            land.append((i, j))
    bomool.append(temp)

dr = [-1, 0, 1, 0]  # 행 상 우 하 좌
dc = [0, 1, 0, -1]  # 열 상 우 하 좌


def bfs(r, c):
    queue = deque([[r, c, 0]])
    visited[r][c] = True
    while queue:
        r, c, distance = queue.popleft()

        for i in range(4):

            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc] or bomool[nr][nc] == 'W':
                continue

            visited[nr][nc] = True
            queue.append([nr, nc, distance + 1])

    return distance


max_ = 0
for i in range(len(land)):
    visited = [[False] * M for _ in range(N)]
    distance = bfs(land[i][0], land[i][1])
    if max_ < distance:
        max_ = distance

print(max_)
