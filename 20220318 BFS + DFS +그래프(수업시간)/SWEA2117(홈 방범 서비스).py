from collections import deque


def bfs(r, c):
    global result_count

    visited[r][c] = True
    queue = deque([[r, c]])
    d = 0  # bfs를 돌면서 거리를 재는 변수
    count = 0  # 각각의 거리마다 집의 개수를 셀 변수
    temp_rev = 0  # 각각의 거리마다 이익을 계산할 변수
    while queue:

        for _ in range(len(queue)):  # 큐의 길이만큼만 돈다.(거리를 재기위해)
            r, c = queue.popleft()

            if city[r][c] == 1:  # 집이라면
                temp_rev += M  # 해당 집의 이익만큼 더해주고
                count += 1  # 개수도 1개 증가

            for i in range(4):  # 델타이동
                nr = r + dr[i]
                nc = c + dc[i]

                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append([nr, nc])

        d += 1  # 거리를 1증가 시켜준다.

        temp_cost = d * d + (d - 1) * (d - 1)  # 각 영역 크기의 면적 계산

        # 만약 집의 개수가 저장된 개수보다 많고 손해를 보지않는다면
        if count > result_count and temp_rev - temp_cost >= 0:
            result_count = count  # 집의 개수를 저장


T = int(input())
dr = [-1, 0, 1, 0]  # 상 우 하 좌
dc = [0, 1, 0, -1]  # 상 우 하 좌
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 도시 크기, 각집의 비용
    city = [list(map(int, input().split())) for _ in range(N)]

    result_count = 0
    for i in range(N):
        for j in range(N):
            visited = [[False] * N for _ in range(N)]
            bfs(i, j)

    print(f'#{tc} {result_count}')
