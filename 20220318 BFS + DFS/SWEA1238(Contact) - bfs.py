from collections import deque

def bfs(start):
    count = 1
    queue = deque([[start, count]])
    visited[start][0] = True

    while queue:
        v, count = queue.popleft()

        for i in graph[v]:
            if not visited[i][0]:
                visited[i][0] = True
                visited[i][1] = count + 1
                queue.append([i, count + 1])


for tc in range(1, 10 + 1):
    N, v = map(int, input().split())

    graph = [[] for _ in range(100 + 1)]  # 그래프 저장
    visited = [[False, 0] for i in range(100 + 1)]  # 방문여부, 방문차례
    info = list(map(int, input().split()))
    for i in range(0, N, 2):  # 그래프 정보를 저장
        from_, to_ = info[i], info[i + 1]
        graph[from_].append(to_)

    bfs(v)  # bfs를 돈다

    max_ = 0  # 전화를 받은 순서중 가장 큰값을 저장
    result = 0  # 큰 값중에서 가장 마지막 사람을 저장

    # 전화를 받은 순서 중 가장 큰 값과 그에 해당하는 가장 큰 번호를 찾는다.
    for i in range(1, 100 + 1):
        if max_ <= visited[i][1]:
            max_ = visited[i][1]
            result = i

    print(f'#{tc} {result}')