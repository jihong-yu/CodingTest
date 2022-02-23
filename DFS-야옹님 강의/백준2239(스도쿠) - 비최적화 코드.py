# 행검사
def row_check(r, c, num):
    for x in range(9):
        if c != x and num == sdoku[r][x]:
            return False
    return True


def col_check(r, c, num):
    # 열검사
    for x in range(9):
        if r != x and num == sdoku[x][c]:
            return False
    return True


def three_check(r, c, num):
    # 3x3 검사
    nc = (c // 3) * 3
    nr = (r // 3) * 3
    for x in range(3):
        for y in range(3):
            if r != nr + x and c != nc + y and sdoku[nr + x][nc + y] == num:
                return False
    return True


def dfs(depth, r, c, num):
    if depth > 0:
        # 행검사
        if not row_check(r, c, num):
            return
        # 열검사
        if not col_check(r, c, num):
            return
        # 3x3 검사
        if not three_check(r, c, num):
            return

    if depth >= len(zero_p):  # 만약 0의 개수에 도달 했다면
        for k in range(9):
            print(''.join(map(str, sdoku[k])))
        exit()

    nr, nc = zero_p[depth]  # 0의 좌표를 dfs를 돈다.
    for j in range(1, 9 + 1):
        sdoku[nr][nc] = j
        dfs(depth + 1, nr, nc, j)
        sdoku[nr][nc] = 0


sdoku = []
zero_p = [] # 2차원 9*9 리스트를 1차원적으로 생각하여 dfs를 돌기 때문에 좌표들을 튜플형식으로 넣는다.
for i in range(9):
    temp = list(map(int, input()))
    for j in range(len(temp)):
        if temp[j] == 0:
            zero_p.append((i, j))
    sdoku.append(temp)

dfs(0, 0, 0, 0)
