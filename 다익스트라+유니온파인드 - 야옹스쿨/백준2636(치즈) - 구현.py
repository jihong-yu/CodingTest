from collections import deque

N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
dr = [-1, 0, 1, 0]  # 상 우 하 좌
dc = [0, 1, 0, -1]  # 상 우 하 좌
pre_cnt = []


def bfs():
    total_time = 0  # 치즈가 녹는데 걸리는 시간
    queue = deque([[0, 0]])  # bfs를 돈다.
    while True:
        loc = set()  # 가장 바깥쪽 치즈들을 좌표들을 담을 셋
        while queue:
            r, c = queue.popleft()

            if cheese[r][c]:  # 만약 치즈가 1이라면
                continue  # 진행x

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc]:  # 범위를 벗어나거나 이미 방문했으면 진행x
                    continue

                if cheese[r][c] == 0 and cheese[nr][nc]:  # 만약 현재칸이 치즈가 없고 다음칸이 치즈가 있으면
                    loc.add((nr, nc))  # 해당 좌표를 저장

                if not cheese[nr][nc]:  # 만약 다음칸에 치즈가 없으면
                    visited[nr][nc] = 1  # 방문처리 후
                    queue.append([nr, nc])  # 해당 위치를 큐에 넣어준다.

        if not len(loc):  # 만약 더이상 녹을 치즈가 없으면
            return total_time  # 총 시간을 리턴

        for i in loc:  # 입력받은 치즈의 위치들을 돌아서
            queue.append([i[0], i[1]])  # 그 위치들을 큐에 넣어주고
            visited[i[0]][i[1]] = 1  # 해당 위치를 방문처리
            cheese[i[0]][i[1]] = 0  # 해당위치의 치즈를 0으로 녹여준다.

        total_time += 1  # 총 걸린 시간을 +1
        pre_cnt.append(len(loc))  # 이번시간에 녹은 치즈의 양을 추가


print(bfs())  # 총걸린시간 출력
print(pre_cnt[-1])  # 가장 마지막 치즈의 양을 출력
