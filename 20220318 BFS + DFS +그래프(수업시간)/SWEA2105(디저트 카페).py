def dfs(n, r, c, d_list):  # 현재 방향
    global result
    global start

    if n == 2 and result >= len(d_list) * 2:
        return

    if n == 3 and r == start[0] and c == start[1]:
        len_ = len(d_list)
        if result < len_:
            result = len_
        return

    # 해당 방향에서 직진하거나 꺽거나
    for i in range(n, n + 2):
        if i == 4:
            continue

        nr = r + dr[i]
        nc = c + dc[i]

        # if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc]:
        #     continue
        #
        # if dessert[nr][nc] in d_list:
        #     continue

        if 0 <= nr < N and 0 <= nc < N and dessert[nr][nc] not in d_list:
            d_list.append(dessert[nr][nc])
            dfs(i, nr, nc, d_list)
            d_list.pop()


dr = [1, 1, -1, -1, 0]  # 좌하 우하, 우상,좌상
dc = [-1, 1, 1, -1, 0]  # 좌하, 우하, 우상, 좌상

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    dessert = [list(map(int, input().split())) for _ in range(N)]
    result = -1

    for i in range(0, N - 2):
        for j in range(1, N - 1):
            start = (i, j)
            dfs(0, i, j, [])

    print(f'#{tc} {result}')
