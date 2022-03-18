import sys

sys.stdin = open('input.txt', 'r')

T = int(input())


def dfs(depth, start):
    global min_

    # N // 2 개를 방문처리했다면
    if depth == N // 2:

        A, B = 0, 0
        # 전체를 검사하면서 1처리가 된것과 되지 않은 것을 나누어서 각각 A,B에 2개씩 더해준다.
        for a in range(N):
            for b in range(N):
                if a >= b:  # 만약 a >=b 라면 검색할 필요가 없기 때문에 continue
                    continue
                if visited[a] and visited[b]:
                    A += (food[a][b] + food[b][a])
                elif not visited[a] and not visited[b]:
                    B += (food[a][b] + food[b][a])

        if abs(A - B) < min_:
            min_ = abs(A - B)

        return

    for i in range(start, N):
        visited[i] = True  # i를 방문처리
        dfs(depth + 1, i + 1)  # i + 1부터 재귀를 돈다.
        visited[i] = False  # 돌고 난 후 다시 방문 False처리


for tc in range(1, T + 1):
    N = int(input())
    food = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N

    min_ = 1 << 60

    dfs(0, 0)

    print(f'#{tc} {min_}')
