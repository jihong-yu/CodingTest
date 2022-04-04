import sys
from collections import deque

sys.stdin = open('input.txt', 'r')


# 각 수마다 방향 처리
def direction(num):
    if num == 1:
        return [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상 우 하 좌
    elif num == 2:
        return [(-1, 0), (1, 0)]  # 상 하
    elif num == 3:
        return [(0, -1), (0, 1)]  # 좌 우
    elif num == 4:
        return [(-1, 0), (0, 1)]  # 상 우
    elif num == 5:
        return [(1, 0), (0, 1)]  # 하 우
    elif num == 6:
        return [(1, 0), (0, -1)]  # 하 좌
    elif num == 7:
        return [(-1, 0), (0, -1)]  # 상 좌


# 해당 방향으로 갈때 가고자 하는 터널로 갈 수 있는 지(터널 연결성 확인)
def direction_check(dr, dc):
    if dr == -1 and dc == 0:  # 상
        return 1, 0  # 하
    elif dr == 0 and dc == 1:  # 우
        return 0, -1  # 좌
    elif dr == 1 and dc == 0:  # 하
        return -1, 0  # 상
    elif dr == 0 and dc == -1:  # 좌
        return 0, 1  # 우


def bfs(r, c):
    queue = deque([[r, c]])
    visited[r][c] = 0
    d = 1  # 거리재기
    while queue:
        # 만약 필요 거리만큼 이동했다면 bfs종료
        if d == L:
            return
        # 큐에 존재하는 길이만큼만 돈다.
        for _ in range(len(queue)):

            r, c = queue.popleft()

            for dr, dc in direction(tunnel[r][c]):
                nr = r + dr
                nc = c + dc

                # 만약 범위를 벗어난다거나 이미 방문했다거나 터널이 없는 경우
                if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc] != -1 or tunnel[nr][nc] == 0:
                    continue

                if direction_check(dr, dc) in direction(tunnel[nr][nc]):  # 터널이 연결되어 있으면
                    visited[nr][nc] = visited[r][c] + 1  # 해당위치를 전의 위치에서 +1 해준다
                    queue.append([nr, nc])

        d += 1  # 거리 1개 추가


T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())  # 세로, 가로, 맨홀세로, 맨홀가로, 소요시간
    tunnel = []
    visited = [[-1 for _ in range(M)] for _ in range(N)]

    for _ in range(N):
        tunnel.append(list(map(int, input().split())))

    bfs(R, C)

    # 개수를 센다.
    count = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 0:  # 만약 해당 위치가 도둑이 갈 수 있는 거리라면
                count += 1

    print(f'#{tc} {count}')
