import sys

sys.setrecursionlimit(2000)

M, N = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(M)]

dr = [-1, 0, 1, 0]  # 상 우 하 좌
dc = [0, 1, 0, -1]  # 상 우 하 좌

# 해당 좌표에서부터 도착지까지 갈 수 있는 경우의 수를 -1로 초기화
visited = [[-1] * N for _ in range(M)]


def dfs(r, c):
    # 만약 도착지에 도달했다면 1을 리턴
    if r == M - 1 and c == N - 1:
        return 1

    # 만약 -1이 아니라면 이미 해당 좌표에서 도착지까지 갈 수 있는 길의
    # 경우의 수가 계산된 것이기 때문에 저장된 경우의 수를 리턴
    if visited[r][c] != -1:
        return visited[r][c]

    # 위의 if에 걸리지 않는다면 해당 좌표에서 횟수를 0으로 설정
    visited[r][c] = 0

    for i in range(4):

        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= M or nc < 0 or nc >= N or miro[nr][nc] >= miro[r][c]:
            continue

        # 해당 좌표에서 탐색 할 수 있는 길로 dfs를 돌고 반환된 값을 모두 더한다
        visited[r][c] += dfs(nr, nc)

    # 만약 모든 탐색이 끝났다면 해당 좌표에 저장된 값을 리턴
    return visited[r][c]


dfs(0, 0)
print(visited[0][0])
