import sys
from collections import deque

sys.stdin = open('input.txt', 'r')


def bfs(start):
    queue = deque([start])
    visited = [[0] * N for _ in range(N)]
    visited[start[0]][start[1]] = 1

    dr = [-1, 0, 1, 0]  # 상우하좌
    dc = [0, 1, 0, -1]  # 상우하좌
    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nc < 0 or nc >= N or nr < 0 or nr >= N or array[nr][nc] == 1:
                continue

            if array[nr][nc] == 3:
                visited[nr][nc] = visited[r][c] + 1
                print(visited)
                return visited[nr][nc] - 2

            elif not visited[nr][nc]:
                visited[nr][nc] = (visited[r][c] + 1)
                queue.append((nr, nc))
    return 0


T = int(input())

for order in range(1, T + 1):
    N = int(input())
    array = []
    start = (-1, -1)
    for i in range(N):
        temp = list(map(int, input()))
        for j in range(len(temp)):
            if temp[j] == 2:
                start = (i, j)
                break
        array.append(temp)

    print(f'#{order} {bfs(start)}')