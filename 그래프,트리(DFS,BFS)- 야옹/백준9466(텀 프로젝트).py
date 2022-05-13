import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs(x, start, cur):
    # 만약 이미 연결처리 되었거나 비연결처리 되었으면
    if temp_cnt[x]:
        for i in visited:  # 이때까지 방문했던 애들은 모두 -1(비연결)처리해준다
            temp_cnt[i] = -1
        return
    # 만약 처음이 아니고 시작점과 같다면
    if cur != 0 and x == start:
        for i in visited:  # 이때까지 방문했던 애들 모두 1(연결) 처리 해준다
            temp_cnt[i] = 1
        return
    # 만약 처음이 아니고 이미 방문했다면 재귀종료
    if cur != 0 and visited.get(x, 0):
        return

    # 해당 지점을 방문처리 해준다.
    visited[x] = 1
    dfs(team[x], start, cur + 1)


T = int(input())

for tc in range(T):
    N = int(input())
    team = [0] + list(map(int, input().split()))
    temp_cnt = {i: 0 for i in range(N + 1)}  # 방문처리를 할 딕셔너리

    # 자기자신은 이미 방문처리
    for i in range(1, N + 1):
        if team[i] == i:
            temp_cnt[i] = 1

    # 각각의 점에서 dfs를 돌면서 방문처리를 해준다.
    for i in range(1, N + 1):
        visited = {}
        dfs(i, i, 0)

    # 방문처리된 정보를 가지고 비연결된 요소들을 찾아 개수를 추가해준다.
    cnt = 0
    for key, value in temp_cnt.items():
        if value <= 0 and key != 0:
            cnt += 1

    print(cnt)
