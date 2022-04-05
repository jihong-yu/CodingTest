def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    parent = [x for x in range(N)]

    x_y = []
    for _ in range(2):
        x_y.append(list(map(int, input().split())))

    graph = []

    E = float(input())

    for i in range(N):
        for j in range(i + 1, N):
            # 거리계산
            x1, y1 = x_y[0][i], x_y[1][i]
            x2, y2 = x_y[0][j], x_y[1][j]
            graph.append((i, j, float((x2 - x1) ** 2 + (y2 - y1) ** 2) * E))

    graph.sort(key=lambda x: x[2])
    ans = 0
    for edge in graph:
        a, b, cost = edge

        v1 = find(a)
        v2 = find(b)

        if v1 != v2:
            parent[v1] = v2
            ans += cost

    print(f'#{tc} {ans:.0f}')
