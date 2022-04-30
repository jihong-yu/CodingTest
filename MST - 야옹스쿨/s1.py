import sys

input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union_(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    parent[a] = b


N = int(input())

parent = [i for i in range(N)]
graph = []
for i in range(N):
    x, y, z = map(int, input().split())
    graph.append((i, x, y, z))  # 각 행성번호를 함께 저장

graph_2 = graph[:]
graph_3 = graph[:]

# 각각의 점을 기준으로 정렬
graph.sort(key=lambda x: x[1])
graph_2.sort(key=lambda x: x[2])
graph_3.sort(key=lambda x: x[3])

# 두점과 그 사이의 거리를 넣을 리스트
distance = []

# 각 지점마다 두점사이의 거리를 계산
for i in range(N - 1):
    cost = abs(graph[i][1] - graph[i + 1][1])
    distance.append((graph[i][0], graph[i + 1][0], cost))

    cost = abs(graph_2[i][2] - graph_2[i + 1][2])
    distance.append((graph_2[i][0], graph_2[i + 1][0], cost))

    cost = abs(graph_3[i][3] - graph_3[i + 1][3])
    distance.append((graph_3[i][0], graph_3[i + 1][0], cost))

# 거리를 기준으로 오름차순
distance.sort(key=lambda x: x[2])

ans = 0
for i in range(len(distance)):

    a, b, cost = distance[i]

    if find(a) != find(b):
        union_(a, b)
        ans += cost

print(ans)
