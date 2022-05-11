direct = {  # 방향 지정
    'D': [1, 0],  # 행 열
    'U': [-1, 0],
    'L': [0, -1],
    'R': [0, 1],
}


# dfs를 돈다.
def dfs(r, c):
    global cnt
    if visited[r][c]:  # 만약 방문했고
        # 아직 방문처리되지 않은 그룹이라면
        if not group_check.get(visited[r][c], 0):
            cnt += 1  # 개수를 +1 해준다.
        group_check[group_num] = 1  # 그 후 해당 그룹은 모드 방문처리해준다.
        return

    visited[r][c] = group_num  # 해당 위치를 해당 그룹으로 표시

    # 해당 방향으로 위치 이동후
    nr = r + direct[arr[r][c]][0]
    nc = c + direct[arr[r][c]][1]
    # dfs를 돈다
    dfs(nr, nc)


N, M = map(int, input().split())
arr = [input() for _ in range(N)]
visited = [[0] * M for _ in range(N)]
group_check = {}  # 해당 그룹이 방문되었는지 체킹
group_num = 1  # 그룹 번호 지정
cnt = 0  # safezone 설치할 개수
for i in range(N):
    for j in range(M):
        if not visited[i][j]:  # 만약 방문하지 않았다면
            dfs(i, j)  # 해당 좌표와 연결된 모든 지점 방문 후
            group_num += 1  # 그룹번호 한개 더 증가

print(cnt)
