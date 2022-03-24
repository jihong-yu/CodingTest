def in_order(v, min_):
    count = count_subtree(tree[v][0])
    if v:
        tree[v][4] += (min_ + count + 1)
        in_order(tree[v][0], min_)
        in_order(tree[v][1], tree[v][4])


def count_subtree(v):
    count = 1

    if v:
        count += count_subtree(tree[v][0])
        count += count_subtree(tree[v][1])
        return count

    return 0


def dfs(cur, depth):
    global max_depth
    visited[cur] = True
    tree[cur][3] = depth
    if max_depth < depth:
        max_depth = depth

    for i in range(2):
        if not visited[tree[cur][i]]:
            dfs(tree[cur][i], depth + 1)


N = int(input())

tree = [[0, 0, 0, 0, 0] for i in range(N + 1)]  # 왼쪽 자식,오른쪽자식, 부모, 깊이 , 너비
for _ in range(N):
    node, left, right = map(int, input().split())

    if left == -1: left = 0
    if right == -1: right = 0

    tree[node][0] = left
    tree[node][1] = right

    tree[left][2] = node
    tree[right][2] = node

visited = [False] * (N + 1)
visited[0] = True

root = 0
for i in range(1, N + 1):
    if tree[i][2] == 0:
        root = i

max_depth = 0

dfs(root, 1)
in_order(root, 0)


depth_list = [[] for _ in range(max_depth + 1)]
for j in range(1, N + 1):
    depth_list[tree[j][3]].append(tree[j][4])

result = []

for i in range(len(depth_list)):
    if len(depth_list[i]) <= 1:
        result.append(1)
    else:
        result.append(max(depth_list[i]) - min(depth_list[i]) + 1)

print(tree)
print(depth_list)
print(result)
print(result.index(max(result), 1), max(result))
