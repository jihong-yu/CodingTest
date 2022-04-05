def dfs(cur):
    visited[cur] = True
    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs(nxt)


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (N + 1)
    ans = 0
    for i in range(1, N + 1):
        if not visited[i]:
            ans += 1
            dfs(i)

    print(f'#{tc} {ans}')
