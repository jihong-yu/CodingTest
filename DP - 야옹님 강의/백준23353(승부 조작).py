def check():
    global ans

    dr = [-1, 0, -1, -1, 1, 0, 1, 1]  # 상 좌 좌상 우상 하 우 우하 좌하
    dc = [0, -1, -1, 1, 0, 1, 1, -1]  # 상 좌 좌상 우상 하 우 우하 좌하

    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                for i in range(8):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        continue

                    if i <= 3:
                        if board[nr][nc] == 1:
                            continue

                    if i >= 4 and board[nr][nc] == 1:
                        cnt = 2
                        start_r, start_c = nr, nc

                        while True:
                            nr = start_r + dr[i]
                            nc = start_c + dc[i]

                            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                                break

                            if board[nr][nc] == 1:
                                cnt += 1
                            else:
                                break

                            start_r = nr
                            start_c = nc

                        if cnt > ans:
                            ans = cnt


def check_2(r, c):
    global ans

    dr = [(-1, 1), (0, 0), (-1, 1), (-1, 1)]  # 상 하 좌 우 좌상 우하 우상 좌하
    dc = [(0, 0), (-1, 1), (-1, 1), (1, -1)]  # 상 하 좌 우 좌상 우하 우상 좌하

    for i in range(4):
        cnt = 1

        for j in range(2):
            nr = r + dr[i][j]
            nc = c + dc[i][j]

            start_r, start_c = nr, nc
            while True:
                if nr < 0 or nr >= N or nc < 0 or nc >= N or board[nr][nc] != 1:
                    break

                cnt += 1
                nr = start_r + dr[i][j]
                nc = start_c + dc[i][j]

                start_r, start_c = nr, nc

        if cnt > ans:
            ans = cnt


def dfs(depth, r, c):
    if depth == 1:
        check_2(r, c)
        return

    for i in range(len(white)):
        board[white[i][0]][white[i][1]] = 1
        dfs(depth + 1, white[i][0], white[i][1])
        board[white[i][0]][white[i][1]] = 2


board = []
white = []
N = int(input())
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 2:
            white.append((i, j))
    board.append(temp)

ans = 1
check()
dfs(0, 0, 0)
print(ans)
