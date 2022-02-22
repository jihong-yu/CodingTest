def dfs(depth):
    global result

    if depth == N:
        temp = 0
        for i in range(len(arr) - 1):
            temp += abs(arr[i] - arr[i + 1])
        if result < temp:
            result = temp
        return
    
    for i in range(N):
        if not visited[i]:
            arr.append(array[i])
            visited[i] = True
            dfs(depth + 1)
            arr.pop()
            visited[i] = False


N = int(input())
visited = [False] * (N + 1)
array = list(map(int, input().split()))
arr = []
result = 0

dfs(0)
print(result)
