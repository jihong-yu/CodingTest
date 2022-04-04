from collections import deque

T = int(input())


# 시작노드와 도착노드를 매개변수로 받는다.
def bfs(s, e):
    global result

    queue = deque([[s, 0]])

    while queue:

        v, distance = queue.popleft()
        if v == e:  # 만약 꺼낸 노드가 도착노드라면
            result = distance  # 해당 거리를 저장 후
            return  # 함수 종료
        for i in graph[v]:
            if not visited[i]:  # 방문하지 않았다면
                visited[i] = True  # 방문 처리후
                queue.append([i, distance + 1])  # 거리를 1늘려주고 큐에 담는다.


for tc in range(1, T + 1):

    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    start, arrival = map(int, input().split())
    visited = [False] * (V + 1)
    result = 0
    bfs(start, arrival)
    print(f'#{tc} {result}')
