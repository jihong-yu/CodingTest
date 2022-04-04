def dfs(r, c, cnt, num):

    if cnt == 6:
        seven_num.add(num)

        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= 4 or nc < 0 or nc >= 4:
            continue

        arr.append(board[nr][nc])
        dfs(nr, nc, cnt + 1, num + str(board[nr][nc]))
        arr.pop()


T = int(input())

dr = [-1, 0, 1, 0]  # 상 우 하 좌
dc = [0, 1, 0, -1]  # 상 우 하 좌

for tc in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(4)]
    arr = []
    seven_num = set()

    for i in range(4):
        for j in range(4):
            dfs(i, j, 0, str(board[i][j]))

    print(f'#{tc} {len(seven_num)}')
