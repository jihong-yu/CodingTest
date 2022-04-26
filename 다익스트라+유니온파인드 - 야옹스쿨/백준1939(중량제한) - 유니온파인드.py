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


N, M = map(int, input().split())

graph = []
for i in range(M):
    a, b, cost = map(int, input().split())
    graph.append([a, b, cost])

graph.sort(key=lambda x: -x[2])  # 가장 중량이 큰 다리를 기준으로 내림차순
parent = [i for i in range(N + 1)]  # 부모를 자기자신으로 설정

v1, v2 = map(int, input().split())

for i in range(M):
    union_(graph[i][0], graph[i][1])  # 두개의 노드를 한 연결요소로 넣어준다

    if find(v1) == find(v2):  # 만약 두 다리가 연결되었다면
        print(graph[i][2])  # 그 때의 중량이 최대 중량이 됨으로 그 값을 출력 후
        break  # 반복문 탈출
