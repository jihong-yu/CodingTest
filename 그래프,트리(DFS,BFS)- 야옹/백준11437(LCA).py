import sys

sys.setrecursionlimit(70000)

input = sys.stdin.readline

N = int(input().rstrip())
graph = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)
visited = [0] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(cur):
    visited[cur] = True

    for nxt in graph[cur]:
        if not visited[nxt]:
            parent[nxt] = cur
            dfs(nxt)


dfs(1)  # 1번노드에서 돌면서 각 노드에서 부모를 저장


# 어느 한 노드부터 부모노드를 찾아나간다.
def search_parent(x, parent_save):
    while x != 0:
        parent_save.append(x)
        x = parent[x]


# 두 정점의 저장된 부모노드를 뒤에서부터 비교한다
def search_common_parent(p1, p2):
    min_index = min(len(p1), len(p2))  # 인덱스가 탐색할 수 있는 최대 범위 설정
    index = -1  # 뒤에서부터 탐색
    while index >= -min_index:  # 인덱스가 범위를 벗어나지 않는다면 반복
        # 비교해서 달라지는 점에서 멈춘다.
        if p1[index] != p2[index]:
            break
        index -= 1

    return p1[index + 1]  # 달라지는점 + 1한 부분이 가장가까운 공통조상노드이다.


# 메모제이션을 위해 구한 부모노드의 값들을 저장해 놓는 리스트 선언
parent_list = [[] for _ in range(N + 1)]
M = int(input())
for _ in range(M):
    parent1 = []  # 첫번째 정점 부모 노드 조사
    parent2 = []  # 두번쨰 정점 부모 노드 조사
    v1, v2 = map(int, input().split())
    if parent_list[v1]:  # 만약 V1이 이미 존재한다면
        parent1 = parent_list[v1]  # 그 값을 대입
    else:  # 존재하지 않는다면
        search_parent(v1, parent1)  # 부모 노드 검색 후
        parent_list[v1] = parent1  # 그 검색기록을 리스트에 저장

    if parent_list[v2]:  # 만약 V2가 이미 존재한다면
        parent2 = parent_list[v2]  # 그 값을 대입
    else:  # 존재하지 않는다면
        search_parent(v2, parent2)  # 부모 노드 검색 후
        parent_list[v2] = parent2  # 그 검색기록을 리스트에 저장

    print(search_common_parent(parent1, parent2))
