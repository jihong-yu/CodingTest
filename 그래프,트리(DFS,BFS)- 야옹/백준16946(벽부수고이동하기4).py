from collections import deque


def zero_group_check(start_r, start_c):
    queue = deque([[start_r, start_c]])
    # 시작번호를 해당 그룹번호로 저장후
    visited[start_r][start_c] = group_num
    group_cnt_dict[group_num] = 1  # 해당 그룹의 0개수를 1로 시작
    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 만약 범위를 벗어나고 이미 방문했거나 벽이라면 continue
            if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc] != 0 or arr[nr][nc] == 1:
                continue
            # 아직 방문하지 않았다면
            visited[nr][nc] = group_num  # 해당 좌표를 같은 그룹번호로 지정 후
            group_cnt_dict[group_num] += 1  # 해당 그룹의 개수를 +1
            queue.append([nr, nc])  # 그후 해당 좌표를 큐에 담는다


def cnt_check(start_r, start_c):
    # 상 하 좌 우 를 돌면서
    for i in range(4):
        nr = start_r + dr[i]
        nc = start_c + dc[i]
        # 만약 범위를 벗어나거나 방문할 수 없거나 0의 개수가 0이라면 continue
        if nr < 0 or nr >= N or nc < 0 or nc >= M or arr[nr][nc] == 1 or not visited[nr][nc]:
            continue
        # 만약 해당그룹을 아직 방문하지 않았다면
        if not group_check.get(visited[nr][nc], 0):
            arr[start_r][start_c] += group_cnt_dict.get(visited[nr][nc], 0)  # 해당 좌표의 개수를 더해주고
            arr[start_r][start_c] %= 10  # 10으로 나눈 나머지를 저장
            group_check[visited[nr][nc]] = 1  # 해당 그룹은 방문으로 저장(같은 그룹의 다른 좌표를 방문하는 것을 방지)


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
dr = [-1, 0, 1, 0]  # 상 우 하 좌
dc = [0, 1, 0, -1]  # 상 우 하 좌
group_num = 1  # 그룹 번호 저장
group_cnt_dict = {}  # 0의 그룹 정보저장

visited = [[0] * M for _ in range(N)]  # 방문처리 및 0의 그룹 정보 저장
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and visited[i][j] == 0:  # 만약 방문할 수 있다면
            zero_group_check(i, j)  # 그룹 정보를 저장하기위해 bfs를 돈다.
            group_num += 1  # 다돌았으면 다음 그룹을 위해 그룹번호를 1 증가시켜준다

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:  # 1의 좌표에서만 조사
            group_check = {}  # 해당 그룹을 방문했는지 조사하기 위한 딕셔너리
            cnt_check(i, j)  # 해당 좌표에서 위아래양옆의 0의 개수를 조사

# 출력
for i in range(N):
    for j in range(M):
        print(arr[i][j], end="")
    print()
