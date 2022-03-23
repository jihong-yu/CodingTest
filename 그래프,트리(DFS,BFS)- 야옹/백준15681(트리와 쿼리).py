import sys

sys.setrecursionlimit(150000)
input = sys.stdin.readline


# dfs로 자식노드의 개수 구하기
def dfs(cur):
    child_count[cur] = 1
    visited[cur] = True

    for nxt in graph[cur]:
        if not visited[nxt]:
            child_count[cur] += dfs(nxt) #하위재귀에서 탐색한 개수를 계속 더해주면서 그 값을 리턴

    return child_count[cur]


N, R, Q = map(int, input().split())  # 정점의 수 , 루트 번호 , 쿼리의 수
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)  # 방문처리
child_count = [0] * (N + 1)  # 한 노드 v 부터 자식노드의 개수를 저장할 리스트
dfs(R)  # dfs를 정점 R부터 돈다.

for _ in range(Q):
    q = int(input().rstrip())
    print(child_count[q])
