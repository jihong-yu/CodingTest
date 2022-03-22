import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(M)]
start_r, start_c, start_dir = map(int, input().split())
end_r, end_c, end_dir = map(int, input().split())

# 문제에서 동 서 남 북 1 2 3 4
dr = [0, 0, 0, 1, -1]  # 행 동 서 남 북
dc = [0, 1, -1, 0, 0]  # 열 동 서 남 북

result = 0  # 결과를 출력할 변수
# 각각의 좌표에 대하여 동서남북 4가지 방향으로 방문처리
visited = [[[False] * 5 for _ in range(N)] for _ in range(M)]


def bfs(r, c, s_dir):
    global result

    queue = deque([[r, c, s_dir, 0]])
    visited[r][c][s_dir] = True
    while queue:
        r, c, c_dir, count = queue.popleft()
        # 만약 도착지점에 도착했다면 횟수 저장후 종료
        if r == end_r - 1 and c == end_c - 1 and c_dir == end_dir:
            result = count
            return

        for i in range(1, 3 + 1):  # 1,2,3 칸을 차례대로 이동한다
            nr = r + (dr[c_dir] * i)
            nc = c + (dc[c_dir] * i)
            # 만약 범위를 벗어나거나 이미 방문했다면 continue
            if nr < 0 or nr >= M or nc < 0 or nc >= N or visited[nr][nc][c_dir]:
                continue

            if miro[nr][nc] == 1:  # 만약 1이 껴있으면 2~3칸은 이동할 수 없으므로 break
                break

            visited[nr][nc][c_dir] = True  # 방문처리
            queue.append([nr, nc, c_dir, count + 1])  # 횟수를 늘려 큐에 담아준다.

        if c_dir == 1 or c_dir == 2:  # 현재가 동,서방향일 때
            if not visited[r][c][3]:  # 남쪽방향을 아직 방문하지 않았다면
                visited[r][c][3] = True  # 방문처리 후 큐에 넣기
                queue.append([r, c, 3, count + 1])
            if not visited[r][c][4]:  # 북쪽방향을 아직 방문하지 않았다면
                visited[r][c][4] = True
                queue.append([r, c, 4, count + 1])
        else:  # 현재가 남,북방향일 때
            if not visited[r][c][1]:  # 동쪽방향을 아직 방문하지 않았다면
                visited[r][c][1] = True
                queue.append([r, c, 1, count + 1])
            if not visited[r][c][2]:  # 서쪽방향을 아직 방문하지 않았다면
                visited[r][c][2] = True
                queue.append([r, c, 2, count + 1])


bfs(start_r - 1, start_c - 1, start_dir)
print(result)
