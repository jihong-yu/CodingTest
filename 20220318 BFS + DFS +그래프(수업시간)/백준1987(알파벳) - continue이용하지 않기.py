R, C = map(int, input().split())

board = [input() for _ in range(R)]
dr = [-1, 1, 0, 0]  # 상 하 좌 우
dc = [0, 0, -1, 1]  # 상 하 좌 우

ans = 0


def dfs(r, c, cnt, trace):
    global ans

    if cnt > ans:
        ans = cnt

    for i in range(4):

        nr = r + dr[i]
        nc = c + dc[i]

        # if nr < 0 or nr >= R or nc < 0 or nc >= C or board[nr][nc] in trace:
        #     continue

        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] not in trace:
            dfs(nr, nc, cnt + 1, trace + board[nr][nc])


dfs(0, 0, 0, board[0][0])
print(ans + 1)
