# 0을 감시되는 위치로 변경
def check(r, c, direct, depth):
    for dr, dc in direct:
        start_r = r  # 현재 위치를 저장
        start_c = c  # 현재 위치를 저장
        while True:  # 해당 방향으로 계속 탐색한다.

            nr = start_r + dr
            nc = start_c + dc

            if nr < 0 or nr >= N or nc >= M or nc < 0 or room[nr][nc] == 6:
                break

            if room[nr][nc] == 0:  # 만약 해당 위치가 0이라면
                room[nr][nc] = depth + 7  # 해당 카메라만의 범위임을 구분짓고 또한 그 값이 6이되면 안되니 +7로 해준다.

            start_r = nr  # 새로운 위치를 현재 위치로
            start_c = nc  # 새로운 위치를 현재 위치로


# 감시되는 위치를 다시 0으로 변경
def un_check(r, c, direct, depth):
    for dr, dc in direct:
        start_r = r
        start_c = c
        while True:

            nr = start_r + dr
            nc = start_c + dc

            if nr < 0 or nr >= N or nc >= M or nc < 0 or room[nr][nc] == 6:
                break

            if room[nr][nc] == depth + 7:  # 만약 depth+7 이라면
                room[nr][nc] = 0  # 다시 0 으로

            start_r = nr
            start_c = nc


# 재귀를 돈다.
def dfs(depth):
    global min_

    if depth == len(cctv):  # 만약 저장된 cctv 모두를 조사했다면
        count = 0  # 개수를 0으로 초기화
        for i in range(N):  # 방을 돌면서 사각지대의 개수를 센다.
            count += room[i].count(0)

        if count < min_:  # 만약 그 개수가 저장된 최솟값보다 작다면
            min_ = count  # 그 값을 최솟값으로 저장
        return  # 재귀 탈출

    if cctv[depth][2] == 1:  # 만약 cctv 1번이라면
        for i in [[(-1, 0)], [(0, 1)], [(1, 0)], [(0, -1)]]:  # 상, 우 , 하, 좌
            check(cctv[depth][0], cctv[depth][1], i, depth)  # cctv범위를 해당 depth + 7 로 바꿔준다.
            dfs(depth + 1)  # 바로 다음 재귀로 이동
            un_check(cctv[depth][0], cctv[depth][1], i, depth)  # 다시 체크한 범위를 0으로 바꿔준다.

    elif cctv[depth][2] == 2:
        for i in [[(-1, 0), (1, 0)], [(0, 1), (0, -1)]]:  # 상하 , 좌우
            check(cctv[depth][0], cctv[depth][1], i, depth)
            dfs(depth + 1)
            un_check(cctv[depth][0], cctv[depth][1], i, depth)

    elif cctv[depth][2] == 3:
        for i in [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(-1, 0), (0, -1)]]:  # 상우, 우하, 하좌 , 좌상
            check(cctv[depth][0], cctv[depth][1], i, depth)
            dfs(depth + 1)
            un_check(cctv[depth][0], cctv[depth][1], i, depth)

    elif cctv[depth][2] == 4:
        for i in [[(-1, 0), (0, 1), (1, 0)], [(-1, 0), (1, 0), (0, -1)], [(-1, 0), (0, 1), (0, -1)],
                  # 상우하, 우하좌, 하좌상, 좌상우
                  [(0, 1), (1, 0), (0, -1)]]:
            check(cctv[depth][0], cctv[depth][1], i, depth)
            dfs(depth + 1)
            un_check(cctv[depth][0], cctv[depth][1], i, depth)

    else:
        for i in [[(-1, 0), (0, 1), (1, 0), (0, -1)]]:  # 상 우 하 좌
            check(cctv[depth][0], cctv[depth][1], i, depth)
            dfs(depth + 1)
            un_check(cctv[depth][0], cctv[depth][1], i, depth)


N, M = map(int, input().split())  # 세로 , 가로
room = []  # 방
cctv = []  # cctv위치 저장

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if 1 <= temp[j] <= 5:  # 만약 1~5 사이라면
            cctv.append((i, j, temp[j]))  # temp[j]를
    room.append(temp)

min_ = 1 << 60
dfs(0)
print(min_)
