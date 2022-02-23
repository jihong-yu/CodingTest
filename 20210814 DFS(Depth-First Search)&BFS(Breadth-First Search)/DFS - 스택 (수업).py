# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

Node, line = map(int, input().split())
graph = [[] for _ in range((Node + 1))]
lines = list(map(int, input().split()))
visited = [False] * (Node + 1)
for i in range(0, len(lines), 2):
    a, b = lines[i], lines[i + 1]
    graph[a].append(b)
    graph[b].append(a)

stack = [1]
visited[1] = True
while stack:

    start = stack.pop()
    print(start, end=" ")
    for i in graph[start][::-1]:
        if not visited[i]:
            visited[i] = True
            stack.append(i)

print()
print(graph)
