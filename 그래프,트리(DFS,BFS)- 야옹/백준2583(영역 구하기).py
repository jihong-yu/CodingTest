import sys
from collections import deque

sys.setrecursionlimit(7000)

input = sys.stdin.readline

M, N, K = map(int, input().split())

map_ = [[0] * (N + 1) for _ in range(M + 1)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())  # 왼쪽 아래, 오른쪽 위
    x1, x2 = x1, x2
    y1, y2 = M - y1, M - y2
    for r in range(y2 + 1, y1 + 1):
        for c in range(x1 + 1, x2 + 1):
            map_[r][c] = 1

dr = [-1, 0, 1, 0]  # 상 우 하 좌
dc = [0, 1, 0, -1]  # 상 우 하 좌


# def bfs(r, c):
#     queue = deque([[r, c]])
#     count = 0
#     map_[r][c] = 1
#     while queue:
#         r, c = queue.popleft()
#         count += 1
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#
#             if nr < 1 or nr >= (M + 1) or nc < 1 or nc >= (N + 1) or map_[nr][nc]:
#                 continue
#             map_[nr][nc] = 1
#             queue.append([nr, nc])
#
#     return count

def dfs(r, c):
    map_[r][c] = 1
    count = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 1 or nr >= (M + 1) or nc < 1 or nc >= (N + 1) or map_[nr][nc]:
            continue

        count += dfs(nr, nc)

    return count


area_count = 0
width = []

for r in range(1, M + 1):
    for c in range(1, N + 1):
        if not map_[r][c]:
            area_count += 1
            width.append(dfs(r, c))

width.sort()
print(area_count)
print(*width)
