def dfs(depth, start):
    global count

    if 0 < depth <= N:
        if sum(result) == S:
            count += 1
        if depth == N:
            return

    for i in range(start, N):
        result.append(arr[i])
        dfs(depth + 1, i + 1)
        result.pop()


N, S = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
result = []
dfs(0, 0)
print(count)
