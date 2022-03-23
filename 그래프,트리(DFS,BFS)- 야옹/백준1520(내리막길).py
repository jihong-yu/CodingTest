import sys

sys.setrecursionlimit(2000)

M, N = map(int, input().split())  # 세로 가로

miro = []
for i in range(M):
    miro.append(list(map(int, input().split())))

visited = [[-1] * N for _ in range(M)]

dr = [-1, 0, 1, 0]  # 상 우 하 좌
dc = [0, 1, 0, -1]  # 상 우 하 좌


def dfs(r, c):
    if r == M - 1 and c == N - 1:
        return 1

    if visited[r][c] != -1:
        return visited[r][c]

    visited[r][c] = 0

    for i in range(4):

        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= M or nc >= N or nc < 0 or miro[nr][nc] >= miro[r][c]:
            continue

        visited[r][c] += dfs(nr, nc)

    return visited[r][c]



count = dfs(0, 0)
for i in range(M):
    print(visited[i])
print(count)
