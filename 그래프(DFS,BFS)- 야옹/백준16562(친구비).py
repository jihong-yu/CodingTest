import sys

sys.setrecursionlimit(3000)

N, M, K = map(int, input().split())
wanted = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
friends = []  # 친구 관계를 담을 리스트(A무리 , B무리 .. 식으로 담음)


# DFS를 돌면서 연결요소 즉 친구무리가 몇개 있는지 확인
def dfs(v, arr):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            dfs(i, arr)


# DFS를 1~N 번까지 돈다.
for i in range(1, N + 1):
    if not visited[i]:
        arr = [i]
        visited[i] = True
        dfs(i, arr)
        friends.append(arr)

result = 0
# 친구무리중 가장 적은 금액을 result에 계속 더해준다.
for friend in friends:
    cost = 1 << 60
    for j in friend:
        if cost > wanted[j]:
            cost = wanted[j]
    result += cost

# 만약 그 값이 가지고 있는 돈보다 적다면
if result <= K:
    print(result)
else:
    print("Oh no")
