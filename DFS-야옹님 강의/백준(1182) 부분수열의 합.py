def dfs(depth, start, num):
    global count

    if 0 < depth <= N:

        if num == S:
            count += 1
        if depth == N:
            return

    for i in range(start, N):
        dfs(depth + 1, i + 1, num + arr[i])


N, S = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

dfs(0, 0, 0)
print(count)
