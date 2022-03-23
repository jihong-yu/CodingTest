N = int(input())
p1, p2 = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

depth = [0 for i in range(N + 1)]
parent = [0 for i in range(N + 1)]
p1_parent = []  # p1 부모 저장
p2_parent = []  # p2 부모 저장


# 해당 노드부터 부모 찾기
def find_parent(x, parent_arr):
    while x != 0:
        parent_arr.append(x)
        x = parent[x]


# 일반 트리 dfs돌기
def dfs(cur, pre):
    for nxt in graph[cur]:
        if nxt == pre:
            continue
        # 깊이 저장
        depth[nxt] = depth[cur] + 1
        # 부모 저장
        parent[nxt] = cur

        dfs(nxt, cur)


for i in range(1, N + 1):
    if depth[i] == 0:
        dfs(i, 0)

# 부모 찾기
find_parent(p1, p1_parent)
find_parent(p2, p2_parent)

# p1,p2 인덱스를 뒤부터 검색
p1_idx = len(p1_parent) - 1
p2_idx = len(p2_parent) - 1

# 둘중 작은 인덱스가 0보다 같거나 클때까지
while min(p1_idx, p2_idx) >= 0:

    # 둘 부모 값이 달라지는 시점에서 break
    if p1_parent[p1_idx] != p2_parent[p2_idx]:
        break
    p1_idx -= 1
    p2_idx -= 1

# 만약 둘의 부모가 하나도 동일하지 않다면 친척이 아님
if p1_idx == len(p1_parent) - 1 and p2_idx == len(p2_parent) - 1:
    print(-1)
else:  # 동일한 부모가 하나라도 있다면
    depth = [0 for i in range(N + 1)]  # 다시 깊이 설정
    dfs(p1_parent[p1_idx + 1], 0)  # 해당 지점을 기준으로 깊이 계산
    print(depth[p1] + depth[p2])  # 해당 깊이를 출력
