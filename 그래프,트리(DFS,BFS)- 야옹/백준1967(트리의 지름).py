import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline
N = int(input().rstrip())
graph = [[] for _ in range(N + 1)]  # 그래프의 정보를 저장할 리스트
visited = [False] * (N + 1)  # 방문처리
cost = [0] * (N + 1)  # 한 정점 v까지 도착할때 드는 비용을 저장할 리스트
for _ in range(N - 1):
    p, c, temp_cost = map(int, input().split())
    graph[p].append([c, temp_cost])
    graph[c].append([p, temp_cost])


# dfs를 돌면서 cost를 확인한다.
def dfs(cur, v_cost):  # 현재노드번호, 비용
    visited[cur] = True
    cost[cur] = v_cost  # 현재비용을 cost로 저장

    for i in graph[cur]:  # 현재 정점에서 갈 수 있는 정점을 돈다.
        if not visited[i[0]]:
            visited[i[0]] = True  # 방문 처리 후
            dfs(i[0], v_cost + i[1])  # 코스트를 더해서 dfs를 돈다.


dfs(1, 0)  # 1번 루트노드에서 각각의 정점까지 비용을 계산
max_lengh = []  # 최대의 비용을 담을 리스트 선언
max_cost = max(cost)  # 최댓값 저장
index_ = -1  # 검사할 인덱스를 -1로 지정
max_count = cost.count(max_cost)  # 최댓값의 개수를 지정
cnt = 0  # 최댓값을 찾은 횟수를 지정
while cnt < max_count:  # 찾은 횟수가 존재하는 최댓값의 개수보다 적다면
    index_ = cost.index(max_cost, index_ + 1)  # 인덱스를 +1해주고 최댓값의 인덱스를 찾는다.
    max_lengh.append(index_)  # 그 인덱스를 저장
    cnt += 1  # 찾은 횟수 1 증가
result = 0  # 결과를 출력할 변수
for i in max_lengh:  # 찾은 최댓값의 인덱스를 돌면서
    visited = [False] * (N + 1)
    dfs(i, 0)  # 다시 dfs를 돌아 가장 큰 비용을 찾는다.
    max_cost = max(cost)  # 가장큰 비용을 찾아
    if result < max_cost:  # 그 값이 저장된 값보다 크면
        result = max_cost  # 그 값을 저장

print(result)
